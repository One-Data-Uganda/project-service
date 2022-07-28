import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_sponsor_sector_industry(
    sponsor_sector_industry_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new sponsor_sector_industry.
    """
    try:
        sponsor_sector_industry = crud.sponsor_sector_industry.create(
            db=db, obj_in=sponsor_sector_industry_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": sponsor_sector_industry}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_sponsor_sector_industry(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get sponsor_sector_industry by ID."""
    r = crud.sponsor_sector_industry.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_sponsor_sector_industry(
    id: uuid.UUID,
    sponsor_sector_industry_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a sponsor_sector_industry.
    """
    sponsor_sector_industry = crud.sponsor_sector_industry.get(db=db, id=id)
    if not sponsor_sector_industry:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_sector_industry = crud.sponsor_sector_industry.update(
        db=db, db_obj=sponsor_sector_industry, obj_in=sponsor_sector_industry_in
    )

    return {"success": True, "data": sponsor_sector_industry}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_sponsor_sector_industry(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a sponsor_sector_industry.
    """
    sponsor_sector_industry = crud.sponsor_sector_industry.get(db=db, id=id)
    if not sponsor_sector_industry:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_sector_industry = crud.sponsor_sector_industry.remove(db=db, id=id)

    return {"success": True, "data": sponsor_sector_industry}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_sponsor_sector_industries(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve sponsor_sector_industries.
    """
    rows = crud.sponsor_sector_industry.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
