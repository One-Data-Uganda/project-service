import os
import uuid
from typing import Any

import aiofiles
from datatables import ColumnDT, DataTables
from fastapi import UploadFile
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logger import log  # noqa:F401
from app.crud.base import CRUDBase
from app.models import (
    FinancialPerformance,
    Power,
    PowerDecision,
    PowerImpact,
    PowerProduct,
    PowerSchedule,
    Project,
    ProjectContact,
    ProjectData,
    ProjectInvestment,
    ProjectLegal,
    ProjectMarket,
    ProjectPartner,
    ProjectStatus,
    ProjectTeam,
    RiskManagement,
    Sponsor,
)
from app.schemas.project import ProjectCreate, ProjectUpdate


class CRUDProject(
    CRUDBase[
        Project,
        ProjectCreate,
        ProjectUpdate,
    ]
):
    def create(self, db: Session, obj_in: ProjectCreate) -> Project:
        r = super().create(db=db, obj_in=obj_in)

        # Now we create all the other records
        for tbl in [
            FinancialPerformance,
            Power,
            PowerDecision,
            PowerImpact,
            PowerProduct,
            PowerSchedule,
            ProjectContact,
            ProjectData,
            ProjectInvestment,
            ProjectLegal,
            ProjectMarket,
            ProjectPartner,
            ProjectTeam,
            RiskManagement,
            Sponsor,
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
        projects = db.query(Project)

        total_count = projects.count()

        if payload.name:
            projects = projects.filter(Project.name.ilike(f"%{payload.name}%"))

        if payload.sectors:
            projects = projects.filter(Project.sector_industry_id.in_(payload.sectors))

        if payload.countries:
            projects = projects.filter(Project.country_id.in_(payload.countries))

        if payload.status_id:
            projects = projects.filter(Project.status_id == payload.status_id)

        if payload.account_id:
            projects = projects.filter(Project.account_id == payload.account_id)

        if payload.project_status:
            subquery = (
                db.query(ProjectStatus.project_id)
                .filter(ProjectStatus.status)
                .in_(payload.project_status)
                .subquery()
            )
            projects = projects.filter(Project.id.in_(subquery.c.project_id))

        r_projects = (
            projects.order_by(Project.featured.desc(), Project.name.asc())
            .limit(payload.pagesize)
            .offset(payload.offset)
        )

        projects = []
        for project in r_projects.all():
            log.debug(project)
            projects.append(
                {
                    "project": project,
                    # "country": Country.query.get(project.country_id),
                    "power": db.get(Power, project.id),
                    "investment": db.get(ProjectInvestment, project.id),
                    # "sector": db.get(Sector, project.sector_id),
                }
            )

        return {"total_count": total_count, "projects": projects}

    # This returns a datatable compatible object
    def json(self, db: Session, account_id: str, params: dict):
        query = (
            db.query()
            .select_from(Project)
            .join(ProjectStatus, Project.current_status_id == ProjectStatus.id)
        )

        if account_id:
            query = query.filter(Project.account_id == account_id)

            columns = [
                ColumnDT(
                    Project.created_at,
                    mData="created_at",
                    search_method="date_range_filter",
                ),
                ColumnDT(Project.name, mData="name"),
                ColumnDT(Project.type, mData="type"),
                ColumnDT(ProjectStatus.status, mData="status"),
                ColumnDT(Project.status_id, mData="status_id"),
                ColumnDT(Project.country_id, mData="country_id"),
                ColumnDT(
                    Project.needs_advisory,
                    mData="needs_advisory",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_investment,
                    mData="needs_investment",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_supply,
                    mData="needs_supply",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_contractor,
                    mData="needs_contractor",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(Project.country_id, mData="country"),
                ColumnDT(Project.id, mData="id"),
            ]
        else:
            columns = [
                ColumnDT(
                    Project.created_at,
                    mData="created_at",
                    search_method="date_range_filter",
                ),
                ColumnDT(Project.account_id, mData="account_id"),
                ColumnDT(Project.name, mData="name"),
                ColumnDT(Project.type, mData="type"),
                ColumnDT(Project.country_id, mData="country_id"),
                ColumnDT(ProjectStatus.status, mData="status"),
                ColumnDT(Project.status_id, mData="status_id"),
                ColumnDT(
                    Project.needs_advisory,
                    mData="needs_advisory",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_investment,
                    mData="needs_investment",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_supply,
                    mData="needs_supply",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(
                    Project.needs_contractor,
                    mData="needs_contractor",
                    search_method="yadcf_autocomplete",
                ),
                ColumnDT(Project.country_id, mData="country"),
                ColumnDT(Project.id, mData="id"),
            ]

        # instantiating a DataTable for the query and table needed
        rowTable = DataTables(params, query, columns)

        # returns what is needed by DataTable
        return rowTable.output_result()


project = CRUDProject(Project)
