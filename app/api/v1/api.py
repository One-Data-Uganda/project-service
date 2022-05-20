from fastapi import APIRouter

from app.api.v1.endpoints import (
    power,
    power_impact,
    power_schedule,
    project,
    project_data,
    project_investment,
    project_market,
    project_team,
    sponsor,
)

api_router = APIRouter()

api_router.include_router(power.router, prefix="/power", tags=["power"])
api_router.include_router(sponsor.router, prefix="/sponsor", tags=["sponsor"])
api_router.include_router(
    power_impact.router, prefix="/power-impact", tags=["power impact"]
)
api_router.include_router(
    power_schedule.router, prefix="/power-schedule", tags=["power schedule"]
)
api_router.include_router(project.router, prefix="/project", tags=["project"])
api_router.include_router(
    project_data.router, prefix="/project-data", tags=["project data"]
)
api_router.include_router(
    project_investment.router, prefix="/project-investment", tags=["project investment"]
)
api_router.include_router(
    project_market.router, prefix="/project-market", tags=["project market"]
)
api_router.include_router(
    project_team.router, prefix="/project-team", tags=["project team"]
)
