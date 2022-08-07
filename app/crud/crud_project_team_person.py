import uuid
from typing import List

from sqlalchemy.orm import Session

from app.core.logger import log  # noqa:F401
from app.crud.base import CRUDBase
from app.models import ProjectTeamPerson
from app.schemas.project_team_person import (
    ProjectTeamPersonCreate,
    ProjectTeamPersonUpdate,
)


class CRUDProjectTeamPerson(
    CRUDBase[
        ProjectTeamPerson,
        ProjectTeamPersonCreate,
        ProjectTeamPersonUpdate,
    ]
):
    def get_for_project(
        self, db: Session, project_id: uuid.UUID, classification: str = None
    ) -> List[ProjectTeamPerson]:
        team_persons = db.query(ProjectTeamPerson).filter(
            ProjectTeamPerson.project_id == project_id
        )

        if classification:
            team_persons = team_persons.filter(
                ProjectTeamPerson.classification == classification
            )

        return team_persons.all()


project_team_person = CRUDProjectTeamPerson(ProjectTeamPerson)
