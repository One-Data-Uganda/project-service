import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_sponsor_type(
    sponsor_type_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new sponsor_type.
    """
    try:
        sponsor_type = crud.sponsor_type.create(db=db, obj_in=sponsor_type_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": sponsor_type}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_sponsor_type(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get sponsor_type by ID."""
    r = crud.sponsor_type.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_sponsor_type(
    id: uuid.UUID,
    sponsor_type_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a sponsor_type.
    """
    sponsor_type = crud.sponsor_type.get(db=db, id=id)
    if not sponsor_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_type = crud.sponsor_type.update(
        db=db, db_obj=sponsor_type, obj_in=sponsor_type_in
    )

    return {"success": True, "data": sponsor_type}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_sponsor_type(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a sponsor_type.
    """
    sponsor_type = crud.sponsor_type.get(db=db, id=id)
    if not sponsor_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_type = crud.sponsor_type.remove(db=db, id=id)

    return {"success": True, "data": sponsor_type}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_sponsor_types(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve sponsor_types.
    """
    rows = crud.sponsor_type.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
