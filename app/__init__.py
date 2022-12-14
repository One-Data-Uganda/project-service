import datetime
import uuid
from typing import Union

import fastapi_plugins
import sentry_sdk
from datatables.search_methods import SEARCH_METHODS
from dateutil.parser import parse as date_parse
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from pydantic import ValidationError
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logger import log


def date_range_filter(expr, value):
    v_from, v_to = value.split("|")
    v_from = (
        date_parse(v_from, dayfirst=True).strftime("%Y-%m-%d 00:00:00")
        if v_from != ""
        else datetime.datetime.now - datetime.interval(days=3650)
    )
    v_to = (
        date_parse(v_to, dayfirst=True).strftime("%Y-%m-%d 23:59:59")
        if v_to != ""
        else datetime.datetime.now()
    )
    return expr.between(v_from, v_to)


def uuid_filter(expr, value):
    return expr == uuid.UUID(value)


SEARCH_METHODS["date_range_filter"] = date_range_filter
SEARCH_METHODS["uuid_filter"] = uuid_filter

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    environment=settings.SENTRY_ENVIRONMENT,
    integrations=[RedisIntegration(), SqlalchemyIntegration()],
)


class AppSettings(
    fastapi_plugins.RedisSettings,
):
    api_name: str = str(__name__)
    redis_url: str = settings.REDIS_URL


app = FastAPI(title=settings.APPLICATION_NAME)

config = AppSettings()


@app.exception_handler(RequestValidationError)
async def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "; ".join([f"{e['loc'][-1]}: {e['msg']}" for e in exc.errors()]),
        },
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc) -> JSONResponse:
    log.error(exc, exc_info=True)
    r = JSONResponse(
        status_code=500, content={"success": False, "message": "System Error"}
    )

    return r


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code, content={"success": False, "message": exc.detail}
    )


@app.on_event("startup")
async def on_startup() -> None:
    await fastapi_plugins.redis_plugin.init_app(app, config=config)
    await fastapi_plugins.redis_plugin.init()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()


app.add_middleware(SentryAsgiMiddleware)

app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
    responses={
        422: {"description": "Validation Error"},
        500: {"description": "Internal Server Error"},
    },
)


if settings.CONFIG_TYPE == "prod":
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({"service.name": settings.APPLICATION_NAME}),
        )
    )
    tracer = trace.get_tracer(__name__)

    jaeger_exporter = JaegerExporter(
        agent_host_name=settings.JAEGER_HOST,
        agent_port=6831,
    )
    # Create a BatchSpanProcessor and add the exporter to it
    span_processor = BatchSpanProcessor(jaeger_exporter)

    # add to the tracer
    trace.get_tracer_provider().add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)
