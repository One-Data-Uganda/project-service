from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import log  # noqa

router = APIRouter()


@router.post("/", response_model=schemas.CountrySectorResponse)
async def create_country_sector(
    country_sector_in: schemas.CountrySectorCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new country_sector.
    """
    try:
        country_sector = crud.country_sector.create(db=db, obj_in=country_sector_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Country Sector with this ID already exists"
        )

    return country_sector


@router.get("/{id}", response_model=schemas.CountrySectorResponse)
async def get_country_sector(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get country sector by ID."""
    r = crud.country_sector.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Country Sector not found")

    return r


@router.put("/{id}", response_model=schemas.CountrySectorResponse)
async def update_country_sector(
    id: str,
    country_sector_in: schemas.CountrySectorUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a country sector.
    """
    country_sector = crud.country_sector.get(db=db, id=id)
    if not country_sector:
        raise HTTPException(status_code=404, detail="Country Sector not found")

    country_sector = crud.country_sector.update(
        db=db, db_obj=country_sector, obj_in=country_sector_in
    )

    return country_sector


@router.delete("/{id}", response_model=schemas.CountrySectorResponse)
async def delete_country_sector(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a country sector.
    """
    country_sector = crud.country_sector.get(db=db, id=id)
    if not country_sector:
        raise HTTPException(status_code=404, detail="Country Sector not found")

    country_sector = crud.country_sector.remove(db=db, id=id)

    return country_sector


@router.get("/", response_model=schemas.CountrySectorListResponse)
async def list_country_sectors(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve country sectors.
    """
    rows = crud.country_sector.get_multi(db, limit=1000)

    return rows
