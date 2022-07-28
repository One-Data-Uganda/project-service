import uuid
from typing import List, Optional

from pydantic import BaseModel

from .capacity import Capacity
from .simple_table import SimpleTable
from .unit import Unit


# Shared properties
class PowerBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    developer: Optional[str]
    notice: Optional[str]
    picture_source: Optional[str]
    picture_title: Optional[str]
    sponsor_id: Optional[uuid.UUID]
    sponsor_name: Optional[str]
    capacity_mw: Optional[float]
    capacity_id: Optional[str]
    size: Optional[float]
    energy_resource_id: Optional[uuid.UUID]
    other_resources: Optional[List[str]]
    technology_id: Optional[uuid.UUID]
    technology_type_id: Optional[uuid.UUID]
    other_technologies: Optional[List[str]]
    waterbody_names: Optional[str]
    scheme: Optional[str]
    design_components: Optional[str]
    unit_id: Optional[str]
    northings: Optional[str]
    eastings: Optional[str]
    northings_intake: Optional[str]
    eastings_intake: Optional[str]
    average_length: Optional[float]
    average_width: Optional[float]
    data_shareable_public: Optional[bool]
    data_shareable_local: Optional[bool]
    main_service_id: Optional[uuid.UUID]
    other_service_ids: Optional[List[str]]
    other_services: Optional[str]
    off_taker_id: Optional[uuid.UUID]
    statutory_permits: Optional[str]
    statutory_licences: Optional[str]
    statutory_agreements: Optional[str]
    power_customer_id: Optional[uuid.UUID]
    other_customer_ids: Optional[List[str]]
    other_customers: Optional[str]
    revenue_source_id: Optional[uuid.UUID]
    other_revenue_sources: Optional[List[str]]
    ppa_status_id: Optional[uuid.UUID]
    ppa_status_grid_id: Optional[uuid.UUID]
    ppa_period: Optional[int]
    outstanding_activities: Optional[str]
    environmental_impacts: Optional[str]
    related_projects: Optional[str]
    investment_description: Optional[str]


# Properties to receive via API on creation
class PowerCreate(PowerBase):
    pass


class PowerUpdate(PowerBase):
    pass


class PowerInDBBase(PowerBase):
    unit: Optional[Unit]
    off_taker: Optional[SimpleTable]
    capacity: Optional[Capacity]
    technology: Optional[SimpleTable]
    technology_type: Optional[SimpleTable]
    energy_resource: Optional[SimpleTable]
    main_service: Optional[SimpleTable]
    power_customer: Optional[SimpleTable]
    revenue_source: Optional[SimpleTable]
    ppa_status: Optional[SimpleTable]
    ppa_status_grid: Optional[SimpleTable]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Power(PowerInDBBase):
    pass


# Additional properties stored in DB
class PowerInDB(PowerInDBBase):
    pass


class PowerResponse(BaseModel):
    success: bool
    data: Power


class PowerListResponse(BaseModel):
    success: bool
    data: Optional[List[Power]]
