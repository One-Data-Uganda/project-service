import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_project_region(
    project_region_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_region.
    """
    try:
        project_region = crud.project_region.create(db=db, obj_in=project_region_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": project_region}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_project_region(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_region by ID."""
    r = crud.project_region.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_project_region(
    id: uuid.UUID,
    project_region_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_region.
    """
    project_region = crud.project_region.get(db=db, id=id)
    if not project_region:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    project_region = crud.project_region.update(
        db=db, db_obj=project_region, obj_in=project_region_in
    )

    return {"success": True, "data": project_region}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_project_region(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_region.
    """
    project_region = crud.project_region.get(db=db, id=id)
    if not project_region:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    project_region = crud.project_region.remove(db=db, id=id)

    return {"success": True, "data": project_region}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_project_regions(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_regions.
    """
    rows = crud.project_region.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
