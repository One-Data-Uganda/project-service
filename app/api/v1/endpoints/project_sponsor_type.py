import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_project_sponsor_type(
    project_sponsor_type_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_sponsor_type.
    """
    try:
        project_sponsor_type = crud.project_sponsor_type.create(
            db=db, obj_in=project_sponsor_type_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": project_sponsor_type}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_project_sponsor_type(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_sponsor_type by ID."""
    r = crud.project_sponsor_type.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_project_sponsor_type(
    id: uuid.UUID,
    project_sponsor_type_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_sponsor_type.
    """
    project_sponsor_type = crud.project_sponsor_type.get(db=db, id=id)
    if not project_sponsor_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    project_sponsor_type = crud.project_sponsor_type.update(
        db=db, db_obj=project_sponsor_type, obj_in=project_sponsor_type_in
    )

    return {"success": True, "data": project_sponsor_type}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_project_sponsor_type(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_sponsor_type.
    """
    project_sponsor_type = crud.project_sponsor_type.get(db=db, id=id)
    if not project_sponsor_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    project_sponsor_type = crud.project_sponsor_type.remove(db=db, id=id)

    return {"success": True, "data": project_sponsor_type}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_project_sponsor_types(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_sponsor_types.
    """
    rows = crud.project_sponsor_type.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
