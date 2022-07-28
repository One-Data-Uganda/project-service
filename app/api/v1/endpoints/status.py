import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_status(
    status_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new status.
    """
    try:
        status = crud.status.create(db=db, obj_in=status_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": status}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_status(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get status by ID."""
    r = crud.status.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_status(
    id: uuid.UUID,
    status_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a status.
    """
    status = crud.status.get(db=db, id=id)
    if not status:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    status = crud.status.update(db=db, db_obj=status, obj_in=status_in)

    return {"success": True, "data": status}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_status(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a status.
    """
    status = crud.status.get(db=db, id=id)
    if not status:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    status = crud.status.remove(db=db, id=id)

    return {"success": True, "data": status}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_statuss(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve statuss.
    """
    rows = crud.status.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
