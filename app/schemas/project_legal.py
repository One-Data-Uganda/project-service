import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectLegalBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    sponsor_status: Optional[str]
    permits_status: Optional[str]
    licenses_status: Optional[str]
    statutory_status: Optional[str]
    jv_status: Optional[str]
    sector_policies: Optional[str]
    sector_laws: Optional[str]
    sector_guidelines: Optional[str]


class ProjectLegalUpdate(ProjectLegalBase):
    pass


# Properties to receive via API on creation
class ProjectLegalCreate(ProjectLegalBase):
    pass


class ProjectLegalInDBBase(ProjectLegalBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectLegal(ProjectLegalInDBBase):
    pass


# Additional properties stored in DB
class ProjectLegalInDB(ProjectLegalInDBBase):
    pass


class ProjectLegalResponse(BaseModel):
    success: bool
    data: Optional[ProjectLegal]


class ProjectLegalListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectLegal]]
