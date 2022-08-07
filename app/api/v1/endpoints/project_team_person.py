import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectTeamPersonResponse)
async def create_project_team_person(
    project_team_person_in: schemas.ProjectTeamPersonCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_team_person.
    """
    try:
        project_team_person = crud.project_team_person.create(
            db=db, obj_in=project_team_person_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectTeamPerson with this ID already exists"
        )

    return {"success": True, "data": project_team_person}


@router.get("/{id}", response_model=schemas.ProjectTeamPersonResponse)
async def get_project_team_person(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_team_person by ID."""
    r = crud.project_team_person.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectTeamPerson not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectTeamPersonResponse)
async def update_project_team_person(
    id: uuid.UUID,
    project_team_person_in: schemas.ProjectTeamPersonUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_team_person.
    """
    project_team_person = crud.project_team_person.get(db=db, id=id)
    if not project_team_person:
        raise HTTPException(status_code=404, detail="ProjectTeamPerson not found")

    project_team_person = crud.project_team_person.update(
        db=db, db_obj=project_team_person, obj_in=project_team_person_in
    )

    return {"success": True, "data": project_team_person}


@router.delete("/{id}", response_model=schemas.ProjectTeamPersonResponse)
async def delete_project_team_person(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_team_person.
    """
    project_team_person = crud.project_team_person.get(db=db, id=id)
    if not project_team_person:
        raise HTTPException(status_code=404, detail="ProjectTeamPerson not found")

    project_team_person = crud.project_team_person.remove(db=db, id=id)

    return {"success": True, "data": project_team_person}


@router.get("/{project_id}/list", response_model=schemas.ProjectTeamPersonListResponse)
async def list_project_team_persons(
    project_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_team_persons.
    """
    rows = crud.project_team_person.get_for_project(db, project_id)

    return {"success": True, "data": rows}
