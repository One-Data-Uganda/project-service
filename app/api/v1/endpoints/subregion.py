from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SubregionResponse)
async def create_subregion(
    subregion_in: schemas.SubregionCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new subregion.
    """
    try:
        subregion = crud.subregion.create(db=db, obj_in=subregion_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Subregion with this ID already exists"
        )

    return subregion


@router.get("/{id}", response_model=schemas.SubregionResponse)
async def get_subregion(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get subregion by ID."""
    r = crud.subregion.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="Subregion not found")

    return r


@router.put("/{id}", response_model=schemas.SubregionResponse)
async def update_subregion(
    id: str,
    subregion_in: schemas.SubregionUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a subregion.
    """
    subregion = crud.subregion.get(db=db, id=id)
    if not subregion:
        raise HTTPException(status_code=404, detail="Subregion not found")

    subregion = crud.subregion.update(db=db, db_obj=subregion, obj_in=subregion_in)

    return subregion


@router.delete("/{id}", response_model=schemas.SubregionResponse)
async def delete_subregion(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a subregion.
    """
    subregion = crud.subregion.get(db=db, id=id)
    if not subregion:
        raise HTTPException(status_code=404, detail="Subregion not found")

    subregion = crud.subregion.remove(db=db, id=id)

    return subregion


@router.get("/", response_model=schemas.SubregionListResponse)
async def list_subregions(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve subregions.
    """
    rows = crud.subregion.get_multi(db, limit=1000)

    return rows
