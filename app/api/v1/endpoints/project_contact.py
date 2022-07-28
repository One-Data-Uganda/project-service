import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectContactResponse)
async def create_project_contact(
    project_contact_in: schemas.ProjectContactCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_contact.
    """
    try:
        project_contact = crud.project_contact.create(db=db, obj_in=project_contact_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectContact with this ID already exists"
        )

    return {"success": True, "data": project_contact}


@router.get("/{id}", response_model=schemas.ProjectContactResponse)
async def get_project_contact(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_contact by ID."""
    r = crud.project_contact.get(db, id)
    log.debug(r.to_dict())
    if not r:
        raise HTTPException(status_code=404, detail="ProjectContact not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectContactResponse)
async def update_project_contact(
    id: uuid.UUID,
    project_contact_in: schemas.ProjectContactUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_contact.
    """
    project_contact = crud.project_contact.get(db=db, id=id)
    if not project_contact:
        raise HTTPException(status_code=404, detail="ProjectContact not found")

    project_contact = crud.project_contact.update(
        db=db, db_obj=project_contact, obj_in=project_contact_in
    )

    return {"success": True, "data": project_contact}


@router.delete("/{id}", response_model=schemas.ProjectContactResponse)
async def delete_project_contact(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_contact.
    """
    project_contact = crud.project_contact.get(db=db, id=id)
    if not project_contact:
        raise HTTPException(status_code=404, detail="ProjectContact not found")

    project_contact = crud.project_contact.remove(db=db, id=id)

    return {"success": True, "data": project_contact}


@router.get("/", response_model=schemas.ProjectContactListResponse)
async def list_project_contacts(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_contacts.
    """
    rows = crud.project_contact.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
