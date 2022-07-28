import os
import uuid
from typing import Any

import aiofiles
from fastapi import UploadFile
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app import models
from app.core.config import settings
from app.core.logger import log  # noqa:F401
from app.crud.base import CRUDBase
from app.schemas.project import ProjectCreate, ProjectUpdate


class CRUDProject(
    CRUDBase[
        models.Project,
        ProjectCreate,
        ProjectUpdate,
    ]
):
    def create(self, db: Session, obj_in: ProjectCreate) -> models.Project:
        r = super().create(db=db, obj_in=obj_in)

        # Now we create all the other records
        for tbl in [
            models.FinancialPerformance,
            models.Power,
            models.PowerDecision,
            models.PowerImpact,
            models.PowerProduct,
            models.PowerSchedule,
            models.ProjectContact,
            models.ProjectData,
            models.ProjectInvestment,
            models.ProjectInvestment,
            models.ProjectLegal,
            models.ProjectMarket,
            models.ProjectPartner,
            models.ProjectTeam,
            models.RiskManagement,
            models.Sponsor,
        ]:
            stmt = insert(tbl).values(id=r.id)
            stmt = stmt.on_conflict_do_nothing()
            db.execute(stmt)
        db.commit()

        return r

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

    def filter(self, db: Session, payload):
        projects = db.query(models.Project)

        total_count = projects.count()

        if payload.name:
            projects = projects.filter(models.Project.name.ilike(f"%{payload.name}%"))

        if payload.sectors:
            projects = projects.filter(
                models.Project.sector_industry_id.in_(payload.sectors)
            )

        if payload.countries:
            projects = projects.filter(models.Project.country_id.in_(payload.countries))

        if payload.status_id:
            projects = projects.filter(models.Project.status_id == payload.status_id)

        if payload.account_id:
            projects = projects.filter(models.Project.account_id == payload.account_id)

        if payload.project_status:
            subquery = (
                db.query(models.ProjectStatus.project_id)
                .filter(models.ProjectStatus.status)
                .in_(payload.project_status)
                .subquery()
            )
            projects = projects.filter(models.Project.id.in_(subquery.c.project_id))

        r_projects = (
            projects.order_by(models.Project.featured.desc(), models.Project.name.asc())
            .limit(payload.pagesize)
            .offset(payload.offset)
        )

        projects = []
        for project in r_projects.all():
            log.debug(project)
            projects.append(
                {
                    "project": project,
                    # "country": models.Country.query.get(project.country_id),
                    "power": db.get(models.Power, project.id),
                    "investment": db.get(models.ProjectInvestment, project.id),
                    # "sector": db.get(models.Sector, project.sector_id),
                }
            )

        return {"total_count": total_count, "projects": projects}


project = CRUDProject(models.Project)
