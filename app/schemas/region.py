from typing import List, Optional

from pydantic import BaseModel

from .sub_region import SubRegion


# Shared properties
class RegionBase(BaseModel):
    name: str


# Properties to receive via API on creation
class RegionCreate(RegionBase):
    pass


class RegionUpdate(RegionBase):
    pass


class RegionInDBBase(RegionBase):
    id: int

    subregions: Optional[List[SubRegion]]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Region(RegionInDBBase):
    pass


# Additional properties stored in DB
class RegionInDB(RegionInDBBase):
    pass


class RegionResponse(BaseModel):
    success: bool
    data: Region


class RegionListResponse(BaseModel):
    success: bool
    data: Optional[List[Region]]
