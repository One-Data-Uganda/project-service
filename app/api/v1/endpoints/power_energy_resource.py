import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_power_energy_resource(
    power_energy_resource_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_energy_resource.
    """
    try:
        power_energy_resource = crud.power_energy_resource.create(
            db=db, obj_in=power_energy_resource_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": power_energy_resource}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_power_energy_resource(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_energy_resource by ID."""
    r = crud.power_energy_resource.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_power_energy_resource(
    id: uuid.UUID,
    power_energy_resource_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_energy_resource.
    """
    power_energy_resource = crud.power_energy_resource.get(db=db, id=id)
    if not power_energy_resource:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_energy_resource = crud.power_energy_resource.update(
        db=db, db_obj=power_energy_resource, obj_in=power_energy_resource_in
    )

    return {"success": True, "data": power_energy_resource}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_power_energy_resource(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_energy_resource.
    """
    power_energy_resource = crud.power_energy_resource.get(db=db, id=id)
    if not power_energy_resource:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_energy_resource = crud.power_energy_resource.remove(db=db, id=id)

    return {"success": True, "data": power_energy_resource}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_power_energy_resources(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_energy_resources.
    """
    rows = crud.power_energy_resource.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
