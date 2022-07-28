import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_power_component(
    power_component_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_component.
    """
    try:
        power_component = crud.power_component.create(db=db, obj_in=power_component_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": power_component}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_power_component(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_component by ID."""
    r = crud.power_component.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_power_component(
    id: uuid.UUID,
    power_component_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_component.
    """
    power_component = crud.power_component.get(db=db, id=id)
    if not power_component:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_component = crud.power_component.update(
        db=db, db_obj=power_component, obj_in=power_component_in
    )

    return {"success": True, "data": power_component}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_power_component(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_component.
    """
    power_component = crud.power_component.get(db=db, id=id)
    if not power_component:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_component = crud.power_component.remove(db=db, id=id)

    return {"success": True, "data": power_component}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_power_components(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_components.
    """
    rows = crud.power_component.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
