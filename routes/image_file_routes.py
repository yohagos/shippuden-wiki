from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from uuid import UUID, uuid4

from database.db import get_db
from services.image_file_service import create_image_file
from models.image_file import ImageFile, ShowImageFile

router = APIRouter(
    prefix="/image",
    tags=["Images"],
)

@router.post("/upload", response_model=ShowImageFile)
async def upload_image(
    subject_id: UUID,
    subject_type: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    content = await file.read()
    image_file = ImageFile(
        subject_id=subject_id,
        subject_type=subject_type,
        id=uuid4(),
        content=content,
        content_type=file.content_type,
        filename=file.filename
    )
    return create_image_file(image_file, db)
