import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class SponsorBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    name: Optional[str]
    short_name: Optional[str]
    other_sponsors: Optional[str]
    shareholders: Optional[str]
    background: Optional[str]
    experience: Optional[str]
    ownership: Optional[str]
    percentage_public: Optional[float]
    percentage_private: Optional[float]
    percentage_academic: Optional[float]
    products: Optional[str]
    other_projects: Optional[str]
    compliance: Optional[str]
    partners: Optional[str]
    capital_statement: Optional[str]
    contact_person: Optional[str]
    contact_address: Optional[str]
    contact_postal: Optional[str]
    contact_email: Optional[str]
    contact_telephone: Optional[str]
    contact_website: Optional[str]
    sponsor_types: Optional[List[str]]
    countries: Optional[List[str]]
    other_countries: Optional[List[str]]
    sector_industry_id: Optional[str]
    other_sectors: Optional[List[str]]
    capital_required: Optional[float]
    capital_available: Optional[float]


# Properties to receive via API on creation
class SponsorCreate(SponsorBase):
    pass


class SponsorUpdate(SponsorBase):
    pass


class SponsorInDBBase(SponsorBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Sponsor(SponsorInDBBase):
    pass


# Additional properties stored in DB
class SponsorInDB(SponsorInDBBase):
    pass


class SponsorResponse(BaseModel):
    success: bool
    data: Optional[Sponsor]


class SponsorListResponse(BaseModel):
    success: bool
    data: Optional[List[Sponsor]]
