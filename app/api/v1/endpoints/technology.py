import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_technology(
    technology_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new technology.
    """
    try:
        technology = crud.technology.create(db=db, obj_in=technology_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": technology}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_technology(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get technology by ID."""
    r = crud.technology.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_technology(
    id: uuid.UUID,
    technology_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a technology.
    """
    technology = crud.technology.get(db=db, id=id)
    if not technology:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    technology = crud.technology.update(db=db, db_obj=technology, obj_in=technology_in)

    return {"success": True, "data": technology}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_technology(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a technology.
    """
    technology = crud.technology.get(db=db, id=id)
    if not technology:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    technology = crud.technology.remove(db=db, id=id)

    return {"success": True, "data": technology}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_technologies(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve technologies.
    """
    rows = crud.technology.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
