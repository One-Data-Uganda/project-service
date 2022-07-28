import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_power_customer(
    power_customer_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_customer.
    """
    try:
        power_customer = crud.power_customer.create(db=db, obj_in=power_customer_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": power_customer}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_power_customer(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_customer by ID."""
    r = crud.power_customer.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_power_customer(
    id: uuid.UUID,
    power_customer_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_customer.
    """
    power_customer = crud.power_customer.get(db=db, id=id)
    if not power_customer:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_customer = crud.power_customer.update(
        db=db, db_obj=power_customer, obj_in=power_customer_in
    )

    return {"success": True, "data": power_customer}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_power_customer(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_customer.
    """
    power_customer = crud.power_customer.get(db=db, id=id)
    if not power_customer:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    power_customer = crud.power_customer.remove(db=db, id=id)

    return {"success": True, "data": power_customer}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_power_customers(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_customers.
    """
    rows = crud.power_customer.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
