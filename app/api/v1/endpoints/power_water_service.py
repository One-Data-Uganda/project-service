import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_power_water_service(
    power_water_service_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_water_service.
    """
    try:
        power_water_service = crud.power_water_service.create(
            db=db, obj_in=power_water_service_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": power_water_service}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_power_water_service(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_water_service by ID."""
    r = crud.power_water_service.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_power_water_service(
    id: uuid.UUID,
    power_water_service_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_water_service.
    """
    power_water_service = crud.power_water_service.get(db=db, id=id)
    if not power_water_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_water_service = crud.power_water_service.update(
        db=db, db_obj=power_water_service, obj_in=power_water_service_in
    )

    return {"success": True, "data": power_water_service}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_power_water_service(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_water_service.
    """
    power_water_service = crud.power_water_service.get(db=db, id=id)
    if not power_water_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_water_service = crud.power_water_service.remove(db=db, id=id)

    return {"success": True, "data": power_water_service}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_power_water_services(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_water_services.
    """
    rows = crud.power_water_service.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
