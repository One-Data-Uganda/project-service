from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import log  # noqa

router = APIRouter()


@router.post("/", response_model=schemas.PowerResponse)
async def create_power(
    power_in: schemas.PowerCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new power.
    """
    try:
        power = crud.power.create(db=db, obj_in=power_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Power with this ID already exists"
        )

    return power


@router.get("/{id}", response_model=schemas.PowerResponse)
async def get_power(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power by ID."""
    r = crud.power.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Power not found")

    return r


@router.put("/{id}", response_model=schemas.PowerResponse)
async def update_power(
    id: str,
    power_in: schemas.PowerUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power.
    """
    power = crud.power.get(db=db, id=id)
    if not power:
        raise HTTPException(status_code=404, detail="Power not found")

    power = crud.power.update(db=db, db_obj=power, obj_in=power_in)

    return power


@router.delete("/{id}", response_model=schemas.PowerResponse)
async def delete_power(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power.
    """
    power = crud.power.get(db=db, id=id)
    if not power:
        raise HTTPException(status_code=404, detail="Power not found")

    power = crud.power.remove(db=db, id=id)

    return power


@router.get("/", response_model=schemas.PowerListResponse)
async def list_powers(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve powers.
    """
    rows = crud.power.get_multi(db, limit=1000)

    return rows
