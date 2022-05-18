import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PowerBase(BaseModel):
    id: Optional[UUID]


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
