import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class SimpleTableBase(BaseModel):
    id: Optional[uuid.UUID]
    name: Optional[str]


class SimpleTableUpdate(SimpleTableBase):
    pass


# Properties to receive via API on creation
class SimpleTableCreate(SimpleTableBase):
    pass


class SimpleTableInDBBase(SimpleTableBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class SimpleTable(SimpleTableInDBBase):
    pass


# Additional properties stored in DB
class SimpleTableInDB(SimpleTableInDBBase):
    pass


class SimpleTableResponse(BaseModel):
    success: bool
    data: Optional[SimpleTable]


class SimpleTableListResponse(BaseModel):
    success: bool
    data: Optional[List[SimpleTable]]
