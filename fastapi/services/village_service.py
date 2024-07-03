from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4, UUID
from base64 import b64encode

from models.villages import Village 
from schemas.village import CreateVillage, ShowVillage, ShowImageFile
from schemas.page_response import PaginationMeta, PaginationResponse

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def all_villages(skip: int, limit: int, db: Session):
    total_items = db.query(Village).count()
    total_pages = (total_items + limit - 1) // limit
    current_page = (skip // limit) + 1
    villages = db.query(Village).offset(skip).limit(limit).all()

    village_data = [
        ShowVillage(
            id=village.id,
            name=village.name,
            description=village.description,
            country=village.country,
            chief=village.chief,
            images=[
                ShowImageFile(
                    id=file.id,
                    filename=file.filename,
                    content=b64encode(file.content).decode("utf-8"),
                    content_type=file.content_type,
                    village_id=file.village_id
                ) for file in village.images
            ]
        ) for village in villages
    ]

    return PaginationResponse(
        data=village_data,
        meta=PaginationMeta(
            total_items=total_items,
            total_pages=total_pages,
            current_page=current_page,
            page_size=limit
        )
    )

def get_village_by_id(village_id: UUID, db: Session):
    logger.info(f"Village by ID")
    return db.query(Village).filter(Village.id == village_id).first()

def create_village(db: Session, req: CreateVillage):
    village = db.query(Village).filter(Village.name == req.name).first()
    logger.info(village)
    if village:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Village {req.name} already exists!"
        )
    new_village = Village(
        id = uuid4(),
        name = req.name,
        description = req.description,
        chief = req.chief,
        country = req.country
    )
    logger.info(new_village)
    db.add(new_village)
    db.commit()
    db.refresh(new_village)
    return new_village
