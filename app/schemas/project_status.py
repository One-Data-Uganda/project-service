import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class ProjectStatusBase(BaseModel):
    project_id: Optional[UUID]
    status: Optional[str]
    user_id: Optional[UUID]
    name: Optional[str]


# Properties to receive via API on creation
class ProjectStatusCreate(ProjectStatusBase):
    pass


class ProjectStatusUpdate(ProjectStatusBase):
    pass


class ProjectStatusInDBBase(ProjectStatusBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectStatus(ProjectStatusInDBBase):
    id: Optional[UUID]
    created_at: Optional[datetime.datetime]


# Additional properties stored in DB
class ProjectStatusInDB(ProjectStatusInDBBase):
    pass


class ProjectStatusResponse(BaseModel):
    success: bool
    data: ProjectStatus


class ProjectStatusListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectStatus]]
