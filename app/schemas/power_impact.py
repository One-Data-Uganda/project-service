from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PowerImpactBase(BaseModel):
    id: Optional[UUID]
    description_environment: Optional[str]
    description_social: Optional[str]
    description_environment_impact: Optional[str]
    description_social_impact: Optional[str]
    treatment_plans: Optional[str]
    occupational_hazards: Optional[str]
    local_regulations: Optional[str]
    sponsor_contribution: Optional[str]
    key_partners: Optional[str]
    environmental_concerns: Optional[str]
    esmp: Optional[str]


# Properties to receive via API on creation
class PowerImpactCreate(PowerImpactBase):
    pass


class PowerImpactUpdate(PowerImpactBase):
    pass


class PowerImpactInDBBase(PowerImpactBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class PowerImpact(PowerImpactInDBBase):
    pass


# Additional properties stored in DB
class PowerImpactInDB(PowerImpactInDBBase):
    pass


class PowerImpactResponse(BaseModel):
    success: bool
    data: PowerImpact


class PowerImpactListResponse(BaseModel):
    success: bool
    data: Optional[List[PowerImpact]]
