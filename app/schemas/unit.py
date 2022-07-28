from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class UnitBase(BaseModel):
    id: Optional[str]
    name: Optional[str]


# Properties to receive via API on creation
class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    pass


class UnitInDBBase(UnitBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Unit(UnitInDBBase):
    pass


# Additional properties stored in DB
class UnitInDB(UnitInDBBase):
    pass


class UnitResponse(BaseModel):
    success: bool
    data: Unit


class UnitListResponse(BaseModel):
    success: bool
    data: Optional[List[Unit]]
