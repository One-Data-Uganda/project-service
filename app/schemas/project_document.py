import uuid
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ProjectDocumentBase(BaseModel):
    id: Optional[uuid.UUID]
    project_id: Optional[uuid.UUID]
    name: Optional[str]
    document_type: Optional[str]
    section: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]


class ProjectDocumentUpdate(ProjectDocumentBase):
    pass


# Properties to receive via API on creation
class ProjectDocumentCreate(ProjectDocumentBase):
    pass


class ProjectDocumentInDBBase(ProjectDocumentBase):
    id: uuid.UUID
    size: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectDocument(ProjectDocumentInDBBase):
    pass


# Additional properties stored in DB
class ProjectDocumentInDB(ProjectDocumentInDBBase):
    pass


class ProjectDocumentResponse(BaseModel):
    success: bool
    data: Optional[ProjectDocument]


class ProjectDocumentListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectDocument]]
