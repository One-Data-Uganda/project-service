import datetime
import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class PowerDecisionBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    commencement_date: Optional[datetime.date]
    client_approval_date: Optional[datetime.date]
    planning_date: Optional[datetime.date]
    equity_finance_date: Optional[datetime.date]
    debt_finance_date: Optional[datetime.date]
    technical_assistance_date: Optional[datetime.date]
    financial_close_date: Optional[datetime.date]
    construction_start_date: Optional[datetime.date]
    commissioning_date: Optional[datetime.date]
    commercial_operations_date: Optional[datetime.date]


# Properties to receive via API on creation
class PowerDecisionCreate(PowerDecisionBase):
    pass


class PowerDecisionUpdate(PowerDecisionBase):
    pass


class PowerDecisionInDBBase(PowerDecisionBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class PowerDecision(PowerDecisionInDBBase):
    pass


# Additional properties stored in DB
class PowerDecisionInDB(PowerDecisionInDBBase):
    pass


class PowerDecisionResponse(BaseModel):
    success: bool
    data: PowerDecision


class PowerDecisionListResponse(BaseModel):
    success: bool
    data: Optional[List[PowerDecision]]
