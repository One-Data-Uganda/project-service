import os
import uuid
from typing import Any, List

import aiofiles
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logger import log  # noqa:F401
from app.crud.base import CRUDBase
from app.models import ProjectDocument
from app.schemas.project_document import ProjectDocumentCreate, ProjectDocumentUpdate


class CRUDProjectDocument(
    CRUDBase[
        ProjectDocument,
        ProjectDocumentCreate,
        ProjectDocumentUpdate,
    ]
):
    def get_for_project(
        self, db: Session, project_id: uuid.UUID, section: str = None, type: str = None
    ) -> List[ProjectDocument]:
        documents = db.query(ProjectDocument).filter(
            ProjectDocument.project_id == project_id
        )

        if section:
            documents = documents.filter(ProjectDocument.section == section)
        if type:
            documents = documents.filter(ProjectDocument.document_type == type)

        return documents.order_by(ProjectDocument.section).all()

    async def save(
        self, db: Session, document_id: uuid.UUID, in_file: UploadFile
    ) -> Any:
        # Save the file
        filepath = os.path.join(
            settings.UPLOADED_FILES_DEST, str(document_id)[:1], str(document_id)
        )
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        async with aiofiles.open(filepath, "wb") as out_file:
            while content := await in_file.read(1024):  # async read chunk
                await out_file.write(content)  # async write chunk

        mimetype = in_file.content_type
        size = os.path.getsize(filepath)

        return {"size": size, "mimetype": mimetype}

    def get_file(self, db: Session, id: uuid.UUID) -> Any:
        document = self.get(db=db, id=id)
        if not document:
            return None

        filepath = os.path.join(
            settings.UPLOADED_PHOTOS_DEST, document.filename[:1], document.filename
        )
        return {
            "project_id": document.project_id,
            "document_type": document.document_type,
            "filepath": filepath,
            "extension": document.extension or "pdf",
        }


project_document = CRUDProjectDocument(ProjectDocument)
