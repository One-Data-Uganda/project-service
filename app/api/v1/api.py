from fastapi import APIRouter

from app.api.v1.endpoints import (
    power,
    project,
)

api_router = APIRouter()
api_router.include_router(power.router, prefix="/power", tags=["power"])
api_router.include_router(project.router, prefix="/project", tags=["project"])
