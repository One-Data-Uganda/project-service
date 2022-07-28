import uuid
from typing import List, Optional

from pydantic import BaseModel

from .simple_table import SimpleTable


# Shared properties
class PowerProductBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    product_service_id: Optional[uuid.UUID]
    other_services: Optional[List[str]]
    product_unit_id: Optional[str]
    annual_output: Optional[float]
    annual_demand: Optional[float]
    primary_customer_id: Optional[uuid.UUID]
    other_customers: Optional[List[str]]
    other_customer_desc: Optional[str]


class PowerProductUpdate(PowerProductBase):
    pass


# Properties to receive via API on creation
class PowerProductCreate(PowerProductBase):
    pass


class PowerProductInDBBase(PowerProductBase):
    id: uuid.UUID

    product_service: Optional[SimpleTable]
    primary_customer: Optional[SimpleTable]

    class Config:
        orm_mode = True


# Additional properties to return via API
class PowerProduct(PowerProductInDBBase):
    pass


# Additional properties stored in DB
class PowerProductInDB(PowerProductInDBBase):
    pass


class PowerProductResponse(BaseModel):
    success: bool
    data: Optional[PowerProduct]


class PowerProductListResponse(BaseModel):
    success: bool
    data: Optional[List[PowerProduct]]
