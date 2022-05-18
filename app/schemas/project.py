import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    id: Optional[UUID]


# Properties to receive via API on creation
class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectInDBBase(ProjectBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Project(ProjectInDBBase):
    pass


# Additional properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass


class ProjectResponse(BaseModel):
    success: bool
    data: Project


class ProjectListResponse(BaseModel):
    success: bool
    data: Optional[List[Project]]
