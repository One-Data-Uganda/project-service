from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PowerBase(BaseModel):
    id: Optional[UUID]
    developer: Optional[str]
    notice: Optional[str]
    picture_source: Optional[str]
    sponsor_id: Optional[UUID]
    full_name: Optional[str]
    short_name: Optional[str]
    capacity_id: Optional[UUID]
    size: Optional[float]
    description: Optional[str]
    sector_id: Optional[str]
    energy_resource_id: Optional[UUID]
    technology_id: Optional[UUID]
    hydropower_type_id: Optional[UUID]
    other_technologies: Optional[str]
    waterbody_names: Optional[str]
    scheme: Optional[str]
    design_components: Optional[str]
    unit_id: Optional[str]
    average_length: Optional[float]
    average_width: Optional[float]
    off_taker_id: Optional[UUID]
    statutory_permits: Optional[str]
    ppa_status_id: Optional[UUID]
    ppa_status_grid_id: Optional[UUID]
    data_shareable_public: Optional[bool]
    data_shareable_local: Optional[bool]


# Properties to receive via API on creation
class PowerCreate(PowerBase):
    pass


class PowerUpdate(PowerBase):
    pass


class PowerInDBBase(PowerBase):
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
