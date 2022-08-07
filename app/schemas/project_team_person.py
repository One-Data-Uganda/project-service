import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectTeamPersonBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    name: Optional[str]
    position: Optional[str]
    qualifications: Optional[str]
    bio: Optional[str]
    picture: Optional[uuid.UUID]
    cv: Optional[uuid.UUID]
    project_id: Optional[uuid.UUID]
    classification: Optional[str]


# Properties to receive via API on creation
class ProjectTeamPersonCreate(ProjectTeamPersonBase):
    pass


class ProjectTeamPersonUpdate(ProjectTeamPersonBase):
    pass


class ProjectTeamPersonInDBBase(ProjectTeamPersonBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectTeamPerson(ProjectTeamPersonInDBBase):
    pass


# Additional properties stored in DB
class ProjectTeamPersonInDB(ProjectTeamPersonInDBBase):
    pass


class ProjectTeamPersonResponse(BaseModel):
    success: bool
    data: ProjectTeamPerson


class ProjectTeamPersonListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectTeamPerson]]
