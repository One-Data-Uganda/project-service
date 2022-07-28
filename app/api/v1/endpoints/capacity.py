import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.CapacityResponse)
async def create_capacity(
    capacity_in: schemas.CapacityCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new capacity.
    """
    try:
        capacity = crud.capacity.create(db=db, obj_in=capacity_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Capacity with this ID already exists"
        )

    return {"success": True, "data": capacity}


@router.get("/{id}", response_model=schemas.CapacityResponse)
async def get_capacity(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get capacity by ID."""
    r = crud.capacity.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="Capacity not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.CapacityResponse)
async def update_capacity(
    id: uuid.UUID,
    capacity_in: schemas.CapacityUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a capacity.
    """
    capacity = crud.capacity.get(db=db, id=id)
    if not capacity:
        raise HTTPException(status_code=404, detail="Capacity not found")

    capacity = crud.capacity.update(db=db, db_obj=capacity, obj_in=capacity_in)

    return {"success": True, "data": capacity}


@router.delete("/{id}", response_model=schemas.CapacityResponse)
async def delete_capacity(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a capacity.
    """
    capacity = crud.capacity.get(db=db, id=id)
    if not capacity:
        raise HTTPException(status_code=404, detail="Capacity not found")

    capacity = crud.capacity.remove(db=db, id=id)

    return {"success": True, "data": capacity}


@router.get("/", response_model=schemas.CapacityListResponse)
async def list_capacities(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve capacities.
    """
    rows = crud.capacity.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
