from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SponsorResponse)
async def create_sponsor(
    sponsor_in: schemas.SponsorCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new sponsor.
    """
    try:
        sponsor = crud.sponsor.create(db=db, obj_in=sponsor_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Sponsor with this ID already exists"
        )

    return {"success": True, "data": sponsor}


@router.get("/{id}", response_model=schemas.SponsorResponse)
async def get_sponsor(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get sponsor by ID."""
    r = crud.sponsor.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Sponsor not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SponsorResponse)
async def update_sponsor(
    id: str,
    sponsor_in: schemas.SponsorUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a sponsor.
    """
    sponsor = crud.sponsor.get(db=db, id=id)
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")

    sponsor = crud.sponsor.update(db=db, db_obj=sponsor, obj_in=sponsor_in)

    return {"success": True, "data": sponsor}


@router.delete("/{id}", response_model=schemas.SponsorResponse)
async def delete_sponsor(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a sponsor.
    """
    sponsor = crud.sponsor.get(db=db, id=id)
    if not sponsor:
        raise HTTPException(status_code=404, detail="Sponsor not found")

    sponsor = crud.sponsor.remove(db=db, id=id)

    return {"success": True, "data": sponsor}


@router.get("/", response_model=schemas.SponsorListResponse)
async def list_sponsors(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve sponsors.
    """
    rows = crud.sponsor.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
