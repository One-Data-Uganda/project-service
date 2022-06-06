import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectDocumentResponse)
async def create_project_document(
    project_id: uuid.UUID,
    name: str,
    document_type: str,
    section: str,
    mimetype: str,
    in_file: UploadFile,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new project_document.
    """
    id = uuid.uuid4()
    try:
        f = await crud.project_document.save(db, id, in_file)
    except Exception as e:
        log.error(e, exc_info=True)
        raise HTTPException(
            status_code=400,
            detail="Failed to save document. Please replace and try again",
        )

    project_document_in = schemas.ProjectDocumentCreate(
        id=id,
        project_id=project_id,
        name=name,
        document_type=document_type,
        section=section,
        size=f["size"],
        mimetype=mimetype,
    )
    try:
        project_document = crud.project_document.create(
            db=db, obj_in=project_document_in
        )
    except Exception:
        project_document = None

    return {"success": True, "data": project_document}


@router.get("/{id}", response_model=schemas.ProjectDocumentResponse)
async def get_project_document(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project document by ID."""
    r = crud.project_document.get(db, id=id)

    if not r:
        raise HTTPException(status_code=401, detail="Project Document not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectDocumentResponse)
async def update_project_document(
    id: uuid.UUID,
    in_file: UploadFile,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project document.
    """
    project_document = crud.project_document.get(db=db, id=id)
    if not project_document:
        raise HTTPException(status_code=404, detail="Project Document not found")

    f = await crud.project_document.save(db, project_document, in_file)

    project_document = crud.project_document.update(
        db=db,
        db_obj=project_document,
        obj_in=schemas.ProjectDocumentUpdate(size=f["size"], mimetype=f["mimetype"]),
    )

    return {"success": True, "data": project_document}


@router.delete("/{id}", response_model=schemas.ProjectDocumentResponse)
async def delete_project_document(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project document.
    """
    project_document = crud.project_document.get(db=db, id=id)
    if not project_document:
        raise HTTPException(status_code=404, detail="Project Document not found")

    project_document = crud.project_document.remove(db=db, id=id)

    return {"success": True, "data": project_document}


@router.get("/{project_id}/list", response_model=schemas.ProjectDocumentListResponse)
async def list_project_documents(
    project_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project documents.
    """
    rows = crud.project_document.get_for_project(db, project_id)

    return {"success": True, "data": rows}


@router.get(
    "/{project_id}/section/{section}",
    response_model=schemas.ProjectDocumentListResponse,
)
async def list_project_documents_by_section(
    project_id: uuid.UUID,
    section: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project documents.
    """
    rows = crud.project_document.get_for_project(db, project_id, section=section)

    return {"success": True, "data": rows}


@router.get(
    "/{project_id}/type/{type}", response_model=schemas.ProjectDocumentListResponse
)
async def list_project_documents_by_type(
    project_id: uuid.UUID,
    type: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project documents.
    """
    rows = crud.project_document.get_for_project(db, project_id, type=type)

    log.debug(rows)

    return {"success": True, "data": rows}
