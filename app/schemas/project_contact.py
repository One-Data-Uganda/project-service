import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectContactBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    project_contact: Optional[str]
    project_address: Optional[str]
    project_postal: Optional[str]
    project_email: Optional[str]
    project_telephone: Optional[str]
    project_website: Optional[str]
    project_nin: Optional[str]
    project_nin_validate: Optional[bool]
    general_contact: Optional[str]
    general_address: Optional[str]
    general_postal: Optional[str]
    general_email: Optional[str]
    general_telephone: Optional[str]
    general_website: Optional[str]
    general_nin: Optional[str]
    general_nin_validate: Optional[bool]


# Properties to receive via API on creation
class ProjectContactCreate(ProjectContactBase):
    pass


class ProjectContactUpdate(ProjectContactBase):
    pass


class ProjectContactInDBBase(ProjectContactBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectContact(ProjectContactInDBBase):
    pass


# Additional properties stored in DB
class ProjectContactInDB(ProjectContactInDBBase):
    pass


class ProjectContactResponse(BaseModel):
    success: bool
    data: ProjectContact


class ProjectContactListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectContact]]
