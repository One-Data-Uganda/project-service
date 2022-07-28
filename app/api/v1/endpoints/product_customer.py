import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_product_customer(
    product_customer_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new product_customer.
    """
    try:
        product_customer = crud.product_customer.create(
            db=db, obj_in=product_customer_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": product_customer}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_product_customer(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get product_customer by ID."""
    r = crud.product_customer.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_product_customer(
    id: uuid.UUID,
    product_customer_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a product_customer.
    """
    product_customer = crud.product_customer.get(db=db, id=id)
    if not product_customer:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    product_customer = crud.product_customer.update(
        db=db, db_obj=product_customer, obj_in=product_customer_in
    )

    return {"success": True, "data": product_customer}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_product_customer(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a product_customer.
    """
    product_customer = crud.product_customer.get(db=db, id=id)
    if not product_customer:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    product_customer = crud.product_customer.remove(db=db, id=id)

    return {"success": True, "data": product_customer}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_product_customers(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve product_customers.
    """
    rows = crud.product_customer.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
