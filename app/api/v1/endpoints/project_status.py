import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectStatusResponse)
async def create_project_status(
    project_status_in: schemas.ProjectStatusCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new project_status.
    """
    project_status = crud.project_status.create(db=db, obj_in=project_status_in)

    # Ideally should use CRUD
    stmt = (
        update(models.Project)
        .values({"current_status_id": project_status.id})
        .where(models.Project.id == project_status.project_id)
    )
    db.execute(stmt)
    db.commit()

    return {"success": True, "data": project_status}


@router.get("/{id}", response_model=schemas.ProjectStatusResponse)
async def get_project_status(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_status by ID."""
    r = crud.project_status.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectStatus not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectStatusResponse)
async def update_project_status(
    id: uuid.UUID,
    project_status_in: schemas.ProjectStatusUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_status.
    """
    project_status = crud.project_status.get(db=db, id=id)
    if not project_status:
        raise HTTPException(status_code=404, detail="ProjectStatus not found")

    project_status = crud.project_status.update(
        db=db, db_obj=project_status, obj_in=project_status_in
    )

    return {"success": True, "data": project_status}


@router.delete("/{id}", response_model=schemas.ProjectStatusResponse)
async def delete_project_status(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_status.
    """
    project_status = crud.project_status.get(db=db, id=id)
    if not project_status:
        raise HTTPException(status_code=404, detail="ProjectStatus not found")

    project_status = crud.project_status.remove(db=db, id=id)

    return {"success": True, "data": project_status}


@router.get("/", response_model=schemas.ProjectStatusListResponse)
async def list_project_statuss(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_statuss.
    """
    rows = crud.project_status.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
