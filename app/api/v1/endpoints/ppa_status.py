import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_ppa_status(
    ppa_status_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new ppa_status.
    """
    try:
        ppa_status = crud.ppa_status.create(db=db, obj_in=ppa_status_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": ppa_status}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_ppa_status(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get ppa_status by ID."""
    r = crud.ppa_status.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_ppa_status(
    id: uuid.UUID,
    ppa_status_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a ppa_status.
    """
    ppa_status = crud.ppa_status.get(db=db, id=id)
    if not ppa_status:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    ppa_status = crud.ppa_status.update(db=db, db_obj=ppa_status, obj_in=ppa_status_in)

    return {"success": True, "data": ppa_status}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_ppa_status(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a ppa_status.
    """
    ppa_status = crud.ppa_status.get(db=db, id=id)
    if not ppa_status:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    ppa_status = crud.ppa_status.remove(db=db, id=id)

    return {"success": True, "data": ppa_status}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_ppa_statuss(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve ppa_statuss.
    """
    rows = crud.ppa_status.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
