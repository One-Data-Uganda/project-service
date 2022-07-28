from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class CapacityBase(BaseModel):
    id: Optional[str]
    name: Optional[str]


# Properties to receive via API on creation
class CapacityCreate(CapacityBase):
    pass


class CapacityUpdate(CapacityBase):
    pass


class CapacityInDBBase(CapacityBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Capacity(CapacityInDBBase):
    pass


# Additional properties stored in DB
class CapacityInDB(CapacityInDBBase):
    pass


class CapacityResponse(BaseModel):
    success: bool
    data: Capacity


class CapacityListResponse(BaseModel):
    success: bool
    data: Optional[List[Capacity]]
