import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    id: Optional[Optional[UUID]]
    name: Optional[str]
    description: Optional[str]
    size: Optional[float]
    investment: Optional[float]
    country_id: Optional[str]
    sector_industry_id: Optional[str]
    sector_group_id: Optional[str]
    sector_division_id: Optional[str]
    sector_id: Optional[str]
    technology: Optional[str]
    status: Optional[str]
    commencement_date: Optional[datetime.date]
    proposed_completion_date: Optional[datetime.date]
    current_stage: Optional[str]
    next_stages: Optional[str]
    estimated_cost: Optional[float]
    contact_information: Optional[str]
    contact_address: Optional[str]
    postal_address: Optional[str]
    telephone: Optional[str]
    email: Optional[str]
    website: Optional[str]
    completed_activities: Optional[str]
    current_activities: Optional[str]
    next_activities: Optional[str]
    outstanding_activities: Optional[str]
    status_id: Optional[str]
    sponsor_type_id: Optional[UUID]
    reference_code: Optional[str]
    manager: Optional[str]
    development_type_id: Optional[UUID]
    development_model: Optional[str]
    percentage_public: Optional[float]
    percentage_private: Optional[float]
    location: Optional[str]
    nearest_town: Optional[str]
    distance: Optional[float]
    nearest_capital_country_id: Optional[str]
    nearest_capital: Optional[str]
    distance_capital: Optional[float]
    environmental_impact: Optional[str]
    social_impact: Optional[str]
    total_investment: Optional[float]
    equity_investment: Optional[float]
    debt_amount: Optional[float]
    grant_amount: Optional[float]
    outstanding_investment: Optional[float]
    related_projects: Optional[str]
    strategy: Optional[str]
    alliances: Optional[str]


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
    data: Optional[Project]


class ProjectListResponse(BaseModel):
    success: bool
    data: Optional[List[Project]]
