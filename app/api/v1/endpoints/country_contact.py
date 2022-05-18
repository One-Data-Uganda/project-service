from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import log  # noqa

router = APIRouter()


@router.post("/", response_model=schemas.CountryContactResponse)
async def create_country_contact(
    country_contact_in: schemas.CountryContactCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new country_contact.
    """
    try:
        country_contact = crud.country_contact.create(db=db, obj_in=country_contact_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Country Contact with this ID already exists"
        )

    return country_contact


@router.get("/{id}", response_model=schemas.CountryContactResponse)
async def get_country_contact(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get country contact by ID."""
    r = crud.country_contact.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Country Contact not found")

    return r


@router.put("/{id}", response_model=schemas.CountryContactResponse)
async def update_country_contact(
    id: str,
    country_contact_in: schemas.CountryContactUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a country contact.
    """
    country_contact = crud.country_contact.get(db=db, id=id)
    if not country_contact:
        raise HTTPException(status_code=404, detail="Country Contact not found")

    country_contact = crud.country_contact.update(
        db=db, db_obj=country_contact, obj_in=country_contact_in
    )

    return country_contact


@router.delete("/{id}", response_model=schemas.CountryContactResponse)
async def delete_country_contact(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a country contact.
    """
    country_contact = crud.country_contact.get(db=db, id=id)
    if not country_contact:
        raise HTTPException(status_code=404, detail="Country Contact not found")

    country_contact = crud.country_contact.remove(db=db, id=id)

    return country_contact


@router.get("/", response_model=schemas.CountryContactListResponse)
async def list_country_contacts(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve country contacts.
    """
    rows = crud.country_contact.get_multi(db, limit=1000)

    return rows
