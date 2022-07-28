import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_development_model(
    development_model_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new development_model.
    """
    try:
        development_model = crud.development_model.create(
            db=db, obj_in=development_model_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": development_model}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_development_model(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get development_model by ID."""
    r = crud.development_model.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_development_model(
    id: uuid.UUID,
    development_model_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a development_model.
    """
    development_model = crud.development_model.get(db=db, id=id)
    if not development_model:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    development_model = crud.development_model.update(
        db=db, db_obj=development_model, obj_in=development_model_in
    )

    return {"success": True, "data": development_model}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_development_model(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a development_model.
    """
    development_model = crud.development_model.get(db=db, id=id)
    if not development_model:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    development_model = crud.development_model.remove(db=db, id=id)

    return {"success": True, "data": development_model}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_development_models(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve development_models.
    """
    rows = crud.development_model.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
