from typing import List, Optional

from pydantic import BaseModel


class Sector(BaseModel):
    id: str
    name: str


# Shared properties
class CountrySectorBase(BaseModel):
    country_id: Optional[str]
    sector_id: Optional[str]
    contribution_to_gdp: Optional[float]
    growth_rate: Optional[float]


# Properties to receive via API on creation
class CountrySectorCreate(CountrySectorBase):
    pass


class CountrySectorUpdate(CountrySectorBase):
    pass


class CountrySectorInDBBase(CountrySectorBase):
    id: int

    sector: Sector

    class Config:
        orm_mode = True


# Additional properties to return via API
class CountrySector(CountrySectorInDBBase):
    pass


# Additional properties stored in DB
class CountrySectorInDB(CountrySectorInDBBase):
    pass


class CountrySectorResponse(BaseModel):
    success: bool
    data: CountrySector


class CountrySectorListResponse(BaseModel):
    success: bool
    data: Optional[List[CountrySector]]
