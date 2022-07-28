import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.PowerProductResponse)
async def create_power_product(
    power_product_in: schemas.PowerProductCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_product.
    """
    try:
        power_product = crud.power_product.create(db=db, obj_in=power_product_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="PowerProduct with this ID already exists"
        )

    return {"success": True, "data": power_product}


@router.get("/{id}", response_model=schemas.PowerProductResponse)
async def get_power_product(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_product by ID."""
    r = crud.power_product.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="PowerProduct not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.PowerProductResponse)
async def update_power_product(
    id: uuid.UUID,
    power_product_in: schemas.PowerProductUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_product.
    """
    power_product = crud.power_product.get(db=db, id=id)
    if not power_product:
        raise HTTPException(status_code=404, detail="PowerProduct not found")

    power_product = crud.power_product.update(
        db=db, db_obj=power_product, obj_in=power_product_in
    )

    return {"success": True, "data": power_product}


@router.delete("/{id}", response_model=schemas.PowerProductResponse)
async def delete_power_product(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_product.
    """
    power_product = crud.power_product.get(db=db, id=id)
    if not power_product:
        raise HTTPException(status_code=404, detail="PowerProduct not found")

    power_product = crud.power_product.remove(db=db, id=id)

    return {"success": True, "data": power_product}


@router.get("/", response_model=schemas.PowerProductListResponse)
async def list_power_products(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_products.
    """
    rows = crud.power_product.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
