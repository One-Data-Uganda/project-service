import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_sponsor_country(
    sponsor_country_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new sponsor_country.
    """
    try:
        sponsor_country = crud.sponsor_country.create(db=db, obj_in=sponsor_country_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": sponsor_country}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_sponsor_country(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get sponsor_country by ID."""
    r = crud.sponsor_country.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_sponsor_country(
    id: uuid.UUID,
    sponsor_country_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a sponsor_country.
    """
    sponsor_country = crud.sponsor_country.get(db=db, id=id)
    if not sponsor_country:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_country = crud.sponsor_country.update(
        db=db, db_obj=sponsor_country, obj_in=sponsor_country_in
    )

    return {"success": True, "data": sponsor_country}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_sponsor_country(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a sponsor_country.
    """
    sponsor_country = crud.sponsor_country.get(db=db, id=id)
    if not sponsor_country:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_country = crud.sponsor_country.remove(db=db, id=id)

    return {"success": True, "data": sponsor_country}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_sponsor_countries(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve sponsor_countries.
    """
    rows = crud.sponsor_country.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
