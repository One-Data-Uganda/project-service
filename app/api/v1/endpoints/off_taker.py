import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_off_taker(
    off_taker_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new off_taker.
    """
    try:
        off_taker = crud.off_taker.create(db=db, obj_in=off_taker_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": off_taker}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_off_taker(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get off_taker by ID."""
    r = crud.off_taker.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_off_taker(
    id: uuid.UUID,
    off_taker_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a off_taker.
    """
    off_taker = crud.off_taker.get(db=db, id=id)
    if not off_taker:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    off_taker = crud.off_taker.update(db=db, db_obj=off_taker, obj_in=off_taker_in)

    return {"success": True, "data": off_taker}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_off_taker(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a off_taker.
    """
    off_taker = crud.off_taker.get(db=db, id=id)
    if not off_taker:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    off_taker = crud.off_taker.remove(db=db, id=id)

    return {"success": True, "data": off_taker}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_off_takers(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve off_takers.
    """
    rows = crud.off_taker.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
