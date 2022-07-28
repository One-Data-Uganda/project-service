import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectLegalResponse)
async def create_project_legal(
    project_legal_in: schemas.ProjectLegalCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_legal.
    """
    try:
        project_legal = crud.project_legal.create(db=db, obj_in=project_legal_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectLegal with this ID already exists"
        )

    return {"success": True, "data": project_legal}


@router.get("/{id}", response_model=schemas.ProjectLegalResponse)
async def get_project_legal(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_legal by ID."""
    r = crud.project_legal.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectLegal not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectLegalResponse)
async def update_project_legal(
    id: uuid.UUID,
    project_legal_in: schemas.ProjectLegalUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_legal.
    """
    project_legal = crud.project_legal.get(db=db, id=id)
    if not project_legal:
        raise HTTPException(status_code=404, detail="ProjectLegal not found")

    project_legal = crud.project_legal.update(
        db=db, db_obj=project_legal, obj_in=project_legal_in
    )

    return {"success": True, "data": project_legal}


@router.delete("/{id}", response_model=schemas.ProjectLegalResponse)
async def delete_project_legal(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_legal.
    """
    project_legal = crud.project_legal.get(db=db, id=id)
    if not project_legal:
        raise HTTPException(status_code=404, detail="ProjectLegal not found")

    project_legal = crud.project_legal.remove(db=db, id=id)

    return {"success": True, "data": project_legal}


@router.get("/", response_model=schemas.ProjectLegalListResponse)
async def list_project_legals(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_legals.
    """
    rows = crud.project_legal.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
