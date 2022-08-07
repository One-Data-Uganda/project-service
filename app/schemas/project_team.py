import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectTeamBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    has_board: Optional[bool]
    has_manager: Optional[bool]
    has_team: Optional[bool]
    number_directors: Optional[int]
    board_directors: Optional[str]
    management_oficers: Optional[str]
    technical_staff: Optional[str]
    management_targets: Optional[str]
    management_agreement: Optional[str]
    personnel_practices: Optional[str]


# Properties to receive via API on creation
class ProjectTeamCreate(ProjectTeamBase):
    pass


class ProjectTeamUpdate(ProjectTeamBase):
    pass


class ProjectTeamInDBBase(ProjectTeamBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectTeam(ProjectTeamInDBBase):
    pass


# Additional properties stored in DB
class ProjectTeamInDB(ProjectTeamInDBBase):
    pass


class ProjectTeamResponse(BaseModel):
    success: bool
    data: ProjectTeam


class ProjectTeamListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectTeam]]
