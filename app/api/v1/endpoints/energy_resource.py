import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_energy_resource(
    energy_resource_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new energy_resource.
    """
    try:
        energy_resource = crud.energy_resource.create(db=db, obj_in=energy_resource_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": energy_resource}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_energy_resource(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get energy_resource by ID."""
    r = crud.energy_resource.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_energy_resource(
    id: uuid.UUID,
    energy_resource_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a energy_resource.
    """
    energy_resource = crud.energy_resource.get(db=db, id=id)
    if not energy_resource:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    energy_resource = crud.energy_resource.update(
        db=db, db_obj=energy_resource, obj_in=energy_resource_in
    )

    return {"success": True, "data": energy_resource}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_energy_resource(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a energy_resource.
    """
    energy_resource = crud.energy_resource.get(db=db, id=id)
    if not energy_resource:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    energy_resource = crud.energy_resource.remove(db=db, id=id)

    return {"success": True, "data": energy_resource}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_energy_resources(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve energy_resources.
    """
    rows = crud.energy_resource.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
