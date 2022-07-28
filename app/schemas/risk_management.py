import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class RiskManagementBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    summary: Optional[str]
    current_partners: Optional[str]
    prospective_partners: Optional[str]
    product_types: Optional[str]
    budget_amount: Optional[float]
    budget_amount_mobilized: Optional[float]
    budget_amount_needed: Optional[float]
    amount: Optional[float]
    guarantees: Optional[str]
    guarantee_types: Optional[str]
    current_guarantee_issuance: Optional[str]
    prospective_guarantee_issuance: Optional[str]
    required_guarantee_amount: Optional[float]
    outstanding_guarantee_amount: Optional[float]
    guarantee_amount_mobilized: Optional[float]
    guarantees_documentation: Optional[str]
    government_support: Optional[str]
    direct_government_support: Optional[str]
    direct_government_value: Optional[float]
    indirect_government_support: Optional[str]
    indirect_government_value: Optional[float]


class RiskManagementUpdate(RiskManagementBase):
    pass


# Properties to receive via API on creation
class RiskManagementCreate(RiskManagementBase):
    pass


class RiskManagementInDBBase(RiskManagementBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class RiskManagement(RiskManagementInDBBase):
    pass


# Additional properties stored in DB
class RiskManagementInDB(RiskManagementInDBBase):
    pass


class RiskManagementResponse(BaseModel):
    success: bool
    data: Optional[RiskManagement]


class RiskManagementListResponse(BaseModel):
    success: bool
    data: Optional[List[RiskManagement]]
