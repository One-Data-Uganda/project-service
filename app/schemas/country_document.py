from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class CountryDocumentBase(BaseModel):
    country_id: Optional[str]
    document_type: Optional[str]
    name: Optional[str]


# Properties to receive via API on creation
class CountryDocumentCreate(CountryDocumentBase):
    pass


class CountryDocumentUpdate(CountryDocumentBase):
    pass


class CountryDocumentInDBBase(CountryDocumentBase):
    id: UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class CountryDocument(CountryDocumentInDBBase):
    pass


# Additional properties stored in DB
class CountryDocumentInDB(CountryDocumentInDBBase):
    pass


class CountryDocumentResponse(BaseModel):
    success: bool
    data: CountryDocument


class CountryDocumentListResponse(BaseModel):
    success: bool
    data: Optional[List[CountryDocument]]
