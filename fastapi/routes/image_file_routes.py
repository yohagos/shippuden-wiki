from fastapi import APIRouter, Depends, UploadFile, File, status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from base64 import b64encode

from database.db import get_db

from services.village_service import get_village_by_id
from services.character_service import get_character_by_id
from services.technique_service import get_technique_by_id

from services.image_file_service import create_image_file, load_images
from schemas.image_file import ShowImageFile
from models.image_files import ImageFile

from schemas.page_response import PaginationResponse

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


router = APIRouter(
    prefix="/image",
    tags=["Images"],
)

def handle_default():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pleas try again"
    )

def village_case(sub_id, db: Session):
    #logger.info(f"village_case: {sub_id}")
    return get_village_by_id(sub_id, db)

def character_case(sub_id, db: Session):
    #logger.info(f"character_case: {sub_id}")
    return get_character_by_id(sub_id, db)

def technique_case(sub_id, db: Session):
    #logger.info(f"technique_case: {sub_id}")
    return get_technique_by_id(sub_id, db)

def switch_case(subject_type, subject_id, db: Session):
    switcher = {
        "village": village_case,
        "character": character_case,
        "technique": technique_case
    }
    func = switcher.get(subject_type, handle_default)
    return func(subject_id, db)

@router.post("/upload")
async def upload_image(
    subject_id: UUID,
    subject_type: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    subject = subject_type.lower()
    obj = switch_case(subject, subject_id, db)
    #logger.info(obj.__dict__)
    
    content = await file.read()
    image_file = ImageFile(
        id=uuid4(),
        content=content,
        content_type=file.content_type,
        filename=file.filename,

        village_id=obj.id if subject.__eq__('village') else None,
        village=obj if subject.__eq__('village') else None,

        character_id=obj.id if subject.__eq__('character') else None,
        character=obj if subject.__eq__('character')  else None,

        technique_id=obj.id if subject.__eq__('technique') else None,
        technique=obj if subject.__eq__('technique') else None,
    )
    #logger.info(image_file.__dict__)
    return create_image_file(image_file, db)

@router.get('s', response_model=PaginationResponse)
def get_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return load_images(skip, limit, db)