import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectMarketBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    overview: Optional[str]
    economic_issues: Optional[str]
    energy_sector: Optional[str]
    electricity_sector: Optional[str]
    sector_policies: Optional[str]
    laws: Optional[str]
    key_stakeholders: Optional[str]
    outlook: Optional[str]
    competition: Optional[str]
    main_competitors: Optional[str]
    competitive_advantage: Optional[str]
    strengths: Optional[str]
    weaknesses: Optional[str]
    opportunities: Optional[str]
    threats: Optional[str]


# Properties to receive via API on creation
class ProjectMarketCreate(ProjectMarketBase):
    pass


class ProjectMarketUpdate(ProjectMarketBase):
    pass


class ProjectMarketInDBBase(ProjectMarketBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectMarket(ProjectMarketInDBBase):
    pass


# Additional properties stored in DB
class ProjectMarketInDB(ProjectMarketInDBBase):
    pass


class ProjectMarketResponse(BaseModel):
    success: bool
    data: ProjectMarket


class ProjectMarketListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectMarket]]
