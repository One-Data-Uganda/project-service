from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class ProjectInvestmentBase(BaseModel):
    id: Optional[UUID]
    total_cost: Optional[float]
    required_investment: Optional[str]
    shareholder_structure: Optional[str]
    equity_investors: Optional[str]
    equity_partners: Optional[str]
    prospective_equity_amount: Optional[float]
    required_equity_amount: Optional[float]
    equity_mobilized: Optional[float]
    equity_needed: Optional[float]
    required_debt_amount: Optional[str]
    current_lenders: Optional[str]
    prospective_lenders: Optional[str]
    loan_type: Optional[str]


# Properties to receive via API on creation
class ProjectInvestmentCreate(ProjectInvestmentBase):
    pass


class ProjectInvestmentUpdate(ProjectInvestmentBase):
    pass


class ProjectInvestmentInDBBase(ProjectInvestmentBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectInvestment(ProjectInvestmentInDBBase):
    pass


# Additional properties stored in DB
class ProjectInvestmentInDB(ProjectInvestmentInDBBase):
    pass


class ProjectInvestmentResponse(BaseModel):
    success: bool
    data: ProjectInvestment


class ProjectInvestmentListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectInvestment]]
