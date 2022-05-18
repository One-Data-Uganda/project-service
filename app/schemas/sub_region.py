from typing import List, Optional

from pydantic import BaseModel

from .country import Country


# Shared properties
class SubRegionBase(BaseModel):
    name: str
    region_id: int


# Properties to receive via API on creation
class SubRegionCreate(SubRegionBase):
    pass


class SubRegionUpdate(SubRegionBase):
    pass


class SubRegionInDBBase(SubRegionBase):
    id: int

    countries: Optional[List[Country]]

    class Config:
        orm_mode = True


# Additional properties to return via API
class SubRegion(SubRegionInDBBase):
    pass


# Additional properties stored in DB
class SubRegionInDB(SubRegionInDBBase):
    pass


class SubRegionResponse(BaseModel):
    success: bool
    data: SubRegion


class SubRegionListResponse(BaseModel):
    success: bool
    data: Optional[List[SubRegion]]
