import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_technology_type(
    technology_type_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new technology_type.
    """
    try:
        technology_type = crud.technology_type.create(db=db, obj_in=technology_type_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": technology_type}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_technology_type(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get technology_type by ID."""
    r = crud.technology_type.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_technology_type(
    id: uuid.UUID,
    technology_type_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a technology_type.
    """
    technology_type = crud.technology_type.get(db=db, id=id)
    if not technology_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    technology_type = crud.technology_type.update(
        db=db, db_obj=technology_type, obj_in=technology_type_in
    )

    return {"success": True, "data": technology_type}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_technology_type(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a technology_type.
    """
    technology_type = crud.technology_type.get(db=db, id=id)
    if not technology_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    technology_type = crud.technology_type.remove(db=db, id=id)

    return {"success": True, "data": technology_type}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_technology_types(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve technology_types.
    """
    rows = crud.technology_type.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
