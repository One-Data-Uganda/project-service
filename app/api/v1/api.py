from fastapi import APIRouter

from app.api.v1.endpoints import (
    capacity,
    development_model,
    development_type,
    energy_resource,
    financial_performance,
    off_taker,
    power,
    power_component,
    power_customer,
    power_decision,
    power_energy_resource,
    power_impact,
    power_power_customer,
    power_product,
    power_schedule,
    power_water_service,
    ppa_status,
    product_customer,
    product_service,
    project,
    project_contact,
    project_country,
    project_data,
    project_document,
    project_investment,
    project_legal,
    project_market,
    project_partner,
    project_region,
    project_sponsor_type,
    project_status,
    project_team,
    project_team_person,
    project_type,
    risk_management,
    sponsor,
    sponsor_country,
    sponsor_document,
    sponsor_sector_industry,
    sponsor_type,
    status,
    technology,
    technology_type,
    unit,
    water_service,
)

api_router = APIRouter()

api_router.include_router(capacity.router, prefix="/capacity", tags=["capacity"])
api_router.include_router(
    development_model.router, prefix="/development-model", tags=["development-model"]
)
api_router.include_router(
    development_type.router, prefix="/development-type", tags=["development-type"]
)
api_router.include_router(
    energy_resource.router, prefix="/energy-resource", tags=["energy-resource"]
)
api_router.include_router(
    financial_performance.router,
    prefix="/financial-performance",
    tags=["financial-performance"],
)
api_router.include_router(off_taker.router, prefix="/off-taker", tags=["off-taker"])
api_router.include_router(power.router, prefix="/power", tags=["power"])
api_router.include_router(
    power_component.router, prefix="/power-component", tags=["power-component"]
)
api_router.include_router(
    power_customer.router, prefix="/power-customer", tags=["power-customer"]
)
api_router.include_router(
    power_decision.router, prefix="/power-decision", tags=["power-decision"]
)
api_router.include_router(
    power_energy_resource.router,
    prefix="/power-energy-resource",
    tags=["power-energy-resource"],
)
api_router.include_router(
    power_impact.router, prefix="/power-impact", tags=["power-impact"]
)
api_router.include_router(
    power_power_customer.router,
    prefix="/power-power-customer",
    tags=["power-power-customer"],
)
api_router.include_router(
    power_product.router, prefix="/power-product", tags=["power-product"]
)
api_router.include_router(
    power_schedule.router, prefix="/power-schedule", tags=["power-schedule"]
)
api_router.include_router(
    power_water_service.router,
    prefix="/power-water-service",
    tags=["power-water-service"],
)
api_router.include_router(ppa_status.router, prefix="/ppa-status", tags=["ppa-status"])
api_router.include_router(
    product_customer.router, prefix="/product-customer", tags=["product-customer"]
)
api_router.include_router(
    product_service.router, prefix="/product-service", tags=["product-service"]
)
api_router.include_router(project.router, prefix="/project", tags=["project"])
api_router.include_router(
    project_contact.router, prefix="/project-contact", tags=["project-contact"]
)
api_router.include_router(
    project_country.router, prefix="/project-country", tags=["project-country"]
)
api_router.include_router(
    project_data.router, prefix="/project-data", tags=["project-data"]
)
api_router.include_router(
    project_document.router, prefix="/project-document", tags=["project-document"]
)
api_router.include_router(
    project_investment.router, prefix="/project-investment", tags=["project-investment"]
)
api_router.include_router(
    project_legal.router, prefix="/project-legal", tags=["project-legal"]
)
api_router.include_router(
    project_market.router, prefix="/project-market", tags=["project-market"]
)
api_router.include_router(
    project_partner.router, prefix="/project-partner", tags=["project-partner"]
)
api_router.include_router(
    project_region.router, prefix="/project-region", tags=["project-region"]
)
api_router.include_router(
    project_sponsor_type.router,
    prefix="/project-sponsor-type",
    tags=["project-sponsor-type"],
)
api_router.include_router(
    project_status.router, prefix="/project-status", tags=["project-status"]
)
api_router.include_router(
    project_team.router, prefix="/project-team", tags=["project-team"]
)
api_router.include_router(
    project_team_person.router,
    prefix="/project-team-person",
    tags=["project-team-person"],
)
api_router.include_router(
    project_type.router, prefix="/project-type", tags=["project-type"]
)
api_router.include_router(
    risk_management.router, prefix="/risk-management", tags=["risk-management"]
)
api_router.include_router(sponsor.router, prefix="/sponsor", tags=["sponsor"])
api_router.include_router(
    sponsor_country.router, prefix="/sponsor-country", tags=["sponsor-country"]
)
api_router.include_router(
    sponsor_document.router, prefix="/sponsor-document", tags=["sponsor-document"]
)
api_router.include_router(
    sponsor_sector_industry.router,
    prefix="/sponsor-sector-industry",
    tags=["sponsor-sector-industry"],
)
api_router.include_router(
    sponsor_type.router, prefix="/sponsor-type", tags=["sponsor-type"]
)
api_router.include_router(status.router, prefix="/status", tags=["status"])
api_router.include_router(technology.router, prefix="/technology", tags=["technology"])
api_router.include_router(
    technology_type.router, prefix="/technology-type", tags=["technology-type"]
)
api_router.include_router(unit.router, prefix="/unit", tags=["unit"])
api_router.include_router(
    water_service.router, prefix="/water-service", tags=["water-service"]
)
