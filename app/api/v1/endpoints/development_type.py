import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_development_type(
    development_type_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new development_type.
    """
    try:
        development_type = crud.development_type.create(
            db=db, obj_in=development_type_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": development_type}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_development_type(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get development_type by ID."""
    r = crud.development_type.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_development_type(
    id: uuid.UUID,
    development_type_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a development_type.
    """
    development_type = crud.development_type.get(db=db, id=id)
    if not development_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    development_type = crud.development_type.update(
        db=db, db_obj=development_type, obj_in=development_type_in
    )

    return {"success": True, "data": development_type}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_development_type(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a development_type.
    """
    development_type = crud.development_type.get(db=db, id=id)
    if not development_type:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    development_type = crud.development_type.remove(db=db, id=id)

    return {"success": True, "data": development_type}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_development_types(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve development_types.
    """
    rows = crud.development_type.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
