from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from base64 import b64encode

from schemas.image_file import ImageFile, ShowImageFile
from schemas.page_response import PaginationMeta, PaginationResponse
from schemas.technique import ShowTechniques, ShowBaseTechniques
from schemas.character import ShowCharacters, ShowBaseCharacter
from schemas.village import ShowVillage, ShowBaseVillage
from models.image_files import ImageFile as ImageModel

import logging

logging.basicConfig(level=logging.info)
logger = logging.getLogger()

def create_image_file(
        file: ImageFile,
        db: Session
):
    files = db.query(ImageModel).all()
    for f in files:
        logger.info(f.__dict__)
    db.add(file)
    db.commit()
    db.refresh(file)
    return ShowImageFile(
        id=file.id,
        filename=file.filename,
        content=b64encode(file.content).decode("utf-8"),
        content_type=file.content_type,
        village=ShowBaseVillage.model_construct(**file.village.__dict__) if file.village else None,
        village_id=file.village_id,
        technique=ShowBaseTechniques.model_construct(**file.technique.__dict__) if file.technique else None,
        technique_id=file.technique_id,
        character=ShowBaseCharacter.model_construct(**file.character.__dict__) if file.character else None,
        character_id=file.character_id,
    )

def load_images(skip: int, limit: int, db: Session):
    total_items = db.query(ImageModel).count()
    total_pages = (total_items + limit - 1) // limit
    current_page = (skip // limit) + 1
    images = db.query(ImageModel).offset(skip).limit(limit).all()
    image_data = [
        ShowImageFile(
            id=image.id,
            filename=image.filename,
            content=b64encode(image.content).decode("utf-8"),
            content_type=image.content_type,
            village=ShowBaseVillage.model_construct(**image.village.__dict__) if image.village else None,
            village_id=image.village_id,
            technique=ShowBaseTechniques.model_construct(**image.technique.__dict__) if image.technique else None,
            technique_id=image.technique_id,
            character=ShowBaseCharacter.model_construct(**image.character.__dict__) if image.character else None,
            character_id=image.character_id,
        ) for image in images
    ]

    return PaginationResponse(
        data=image_data,
        meta=PaginationMeta(
            total_items=total_items,
            total_pages=total_pages,
            current_page=current_page,
            page_size=limit
        )
    )