import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectResponse)
async def create_project(
    project_in: schemas.ProjectCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project.
    """
    try:
        project = crud.project.create(db=db, obj_in=project_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Project with this ID already exists"
        )

    return {"success": True, "data": project}


@router.get("/{id}", response_model=schemas.ProjectResponse)
async def get_project(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project by ID."""
    r = crud.project.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectResponse)
async def update_project(
    id: uuid.UUID,
    project_in: schemas.ProjectUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)

    return {"success": True, "data": project}


@router.delete("/{id}", response_model=schemas.ProjectResponse)
async def delete_project(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project = crud.project.remove(db=db, id=id)

    return {"success": True, "data": project}


@router.post("/filter")
async def filter_projects(
    payload: schemas.ProjectFilterModel,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve projects.
    """
    rows = crud.project.filter(db, payload)

    return {"success": True, "data": rows}


@router.get("/{account_id}/json")
async def project_json(
    account_id: uuid.UUID,
    params: dict,
    db: Session = Depends(deps.get_db),
) -> Any:
    rows = crud.project.json(db, account_id=account_id, params=params)

    return rows


@router.get("/", response_model=schemas.ProjectListResponse)
async def list_projects(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve projects.
    """
    rows = crud.project.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
