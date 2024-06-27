from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Annotated

from database.db import get_db
from models.village import Village as VillageModel, ShowVillage, CreateVillage
from schemas.villages import Village as VillageSchema
from services.village import all_villages, create_village

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/village",
    tags=["Villages"],
)

@router.get('s', response_model=List[ShowVillage])
def get_villages(db: Session =Depends(get_db)):
    return all_villages(db)

@router.post('', response_model=ShowVillage)
def add_village(village_req: CreateVillage, db: Session = Depends(get_db)):
    return create_village(db, village_req)

@router.post('/file')
async def file_upload(file: UploadFile = File()):
    logger.info(await file.read())
    logger.info(file.size)
    logger.info(file.content_type)
    return

@router.post('/file2')
def file_upload_2(file: UploadFile = File()):
    #logger.info(file)
    file_content = file.file.read()
    logger.info(file_content)
    file_bytes = bytearray(file_content)
    logger.info(file_bytes)
    return