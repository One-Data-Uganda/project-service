import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_product_service(
    product_service_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new product_service.
    """
    try:
        product_service = crud.product_service.create(db=db, obj_in=product_service_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": product_service}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_product_service(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get product_service by ID."""
    r = crud.product_service.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_product_service(
    id: uuid.UUID,
    product_service_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a product_service.
    """
    product_service = crud.product_service.get(db=db, id=id)
    if not product_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    product_service = crud.product_service.update(
        db=db, db_obj=product_service, obj_in=product_service_in
    )

    return {"success": True, "data": product_service}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_product_service(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a product_service.
    """
    product_service = crud.product_service.get(db=db, id=id)
    if not product_service:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    product_service = crud.product_service.remove(db=db, id=id)

    return {"success": True, "data": product_service}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_product_services(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve product_services.
    """
    rows = crud.product_service.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
