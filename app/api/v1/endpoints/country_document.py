from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.CountryDocumentResponse)
async def create_country_document(
    country_document_in: schemas.CountryDocumentCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new country_document.
    """
    try:
        country_document = crud.country_document.create(
            db=db, obj_in=country_document_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="Country Document with this ID already exists"
        )

    return country_document


@router.get("/{id}", response_model=schemas.CountryDocumentResponse)
async def get_country_document(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get country document by ID."""
    r = crud.country_document.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Country Document not found")

    return r


@router.put("/{id}", response_model=schemas.CountryDocumentResponse)
async def update_country_document(
    id: str,
    country_document_in: schemas.CountryDocumentUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a country document.
    """
    country_document = crud.country_document.get(db=db, id=id)
    if not country_document:
        raise HTTPException(status_code=404, detail="Country Document not found")

    country_document = crud.country_document.update(
        db=db, db_obj=country_document, obj_in=country_document_in
    )

    return country_document


@router.delete("/{id}", response_model=schemas.CountryDocumentResponse)
async def delete_country_document(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a country document.
    """
    country_document = crud.country_document.get(db=db, id=id)
    if not country_document:
        raise HTTPException(status_code=404, detail="Country Document not found")

    country_document = crud.country_document.remove(db=db, id=id)

    return country_document


@router.get("/", response_model=schemas.CountryDocumentListResponse)
async def list_country_documents(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve country documents.
    """
    rows = crud.country_document.get_multi(db, limit=1000)

    return rows
