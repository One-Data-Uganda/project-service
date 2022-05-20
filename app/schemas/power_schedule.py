from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PowerScheduleBase(BaseModel):
    id: Optional[UUID]
    construction_schedule: Optional[str]
    startup_schedule: Optional[str]
    operations_schedule: Optional[str]
    expenditures: Optional[str]
    funding_schedule: Optional[str]
    regulatory_compliance: Optional[str]


# Properties to receive via API on creation
class PowerScheduleCreate(PowerScheduleBase):
    pass


class PowerScheduleUpdate(PowerScheduleBase):
    pass


class PowerScheduleInDBBase(PowerScheduleBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class PowerSchedule(PowerScheduleInDBBase):
    pass


# Additional properties stored in DB
class PowerScheduleInDB(PowerScheduleInDBBase):
    pass


class PowerScheduleResponse(BaseModel):
    success: bool
    data: PowerSchedule


class PowerScheduleListResponse(BaseModel):
    success: bool
    data: Optional[List[PowerSchedule]]
