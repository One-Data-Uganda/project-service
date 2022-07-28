import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectInvestmentBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    investment_strategy: Optional[str]
    total_cost: Optional[float]
    required_investment: Optional[str]
    shareholder_structure: Optional[str]
    equity_investors: Optional[str]
    equity_partners: Optional[str]
    prospective_equity_amount: Optional[float]
    required_equity_amount: Optional[float]
    equity_mobilized: Optional[float]
    equity_needed: Optional[float]
    required_debt_amount: Optional[float]
    debt_description: Optional[str]
    current_lenders: Optional[str]
    prospective_lenders: Optional[str]
    loan_type: Optional[str]
    other_loan_types: Optional[List[str]]
    other_loan_description: Optional[str]
    loan_amount: Optional[float]
    loan_mobilized: Optional[float]
    loan_needing_mobilization: Optional[float]
    proposed_grant_amount: Optional[str]
    grant_providers: Optional[str]
    prospective_grant_providers: Optional[str]
    grant_types: Optional[str]
    grant_amount: Optional[float]
    grant_mobilized: Optional[float]
    grant_needing_mobilization: Optional[float]
    total_mobilized: Optional[float]
    total_needing_mobilization: Optional[float]


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
