import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectPartnerBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    equity_partners: Optional[str]
    debt_partners: Optional[str]
    tehcnical_advisors: Optional[str]
    implementation_partners: Optional[str]
    institutional_partners: Optional[str]
    stakeholders: Optional[str]


class ProjectPartnerUpdate(ProjectPartnerBase):
    pass


# Properties to receive via API on creation
class ProjectPartnerCreate(ProjectPartnerBase):
    pass


class ProjectPartnerInDBBase(ProjectPartnerBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectPartner(ProjectPartnerInDBBase):
    pass


# Additional properties stored in DB
class ProjectPartnerInDB(ProjectPartnerInDBBase):
    pass


class ProjectPartnerResponse(BaseModel):
    success: bool
    data: Optional[ProjectPartner]


class ProjectPartnerListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectPartner]]
