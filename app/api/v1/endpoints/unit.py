import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_unit(
    unit_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new unit.
    """
    try:
        unit = crud.unit.create(db=db, obj_in=unit_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": unit}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_unit(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get unit by ID."""
    r = crud.unit.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_unit(
    id: uuid.UUID,
    unit_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a unit.
    """
    unit = crud.unit.get(db=db, id=id)
    if not unit:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    unit = crud.unit.update(db=db, db_obj=unit, obj_in=unit_in)

    return {"success": True, "data": unit}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_unit(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a unit.
    """
    unit = crud.unit.get(db=db, id=id)
    if not unit:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    unit = crud.unit.remove(db=db, id=id)

    return {"success": True, "data": unit}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_units(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve units.
    """
    rows = crud.unit.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
