import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_water_service(
    water_service_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new water_service.
    """
    try:
        water_service = crud.water_service.create(db=db, obj_in=water_service_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": water_service}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_water_service(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get water_service by ID."""
    r = crud.water_service.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_water_service(
    id: uuid.UUID,
    water_service_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a water_service.
    """
    water_service = crud.water_service.get(db=db, id=id)
    if not water_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    water_service = crud.water_service.update(
        db=db, db_obj=water_service, obj_in=water_service_in
    )

    return {"success": True, "data": water_service}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_water_service(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a water_service.
    """
    water_service = crud.water_service.get(db=db, id=id)
    if not water_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    water_service = crud.water_service.remove(db=db, id=id)

    return {"success": True, "data": water_service}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_water_services(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve water_services.
    """
    rows = crud.water_service.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
