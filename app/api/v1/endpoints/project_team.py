from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectTeamResponse)
async def create_project_team(
    project_team_in: schemas.ProjectTeamCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new project_team.
    """
    try:
        project_team = crud.project_team.create(db=db, obj_in=project_team_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Project Team with this ID already exists"
        )

    return {"success": True, "data": project_team}


@router.get("/{id}", response_model=schemas.ProjectTeamResponse)
async def get_project_team(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project team by ID."""
    r = crud.project_team.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Project Team not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectTeamResponse)
async def update_project_team(
    id: str,
    project_team_in: schemas.ProjectTeamUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project team.
    """
    project_team = crud.project_team.get(db=db, id=id)
    if not project_team:
        raise HTTPException(status_code=404, detail="Project Team not found")

    project_team = crud.project_team.update(
        db=db, db_obj=project_team, obj_in=project_team_in
    )

    return {"success": True, "data": project_team}


@router.delete("/{id}", response_model=schemas.ProjectTeamResponse)
async def delete_project_team(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project team.
    """
    project_team = crud.project_team.get(db=db, id=id)
    if not project_team:
        raise HTTPException(status_code=404, detail="Project Team not found")

    project_team = crud.project_team.remove(db=db, id=id)

    return {"success": True, "data": project_team}


@router.get("/", response_model=schemas.ProjectTeamListResponse)
async def list_project_teams(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project teams.
    """
    rows = crud.project_team.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
