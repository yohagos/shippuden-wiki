from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from schemas.villages import Village as VillageSchema
from models.village import Village as VillageModel, CreateVillage

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def all_villages(db: Session):
    return db.query(VillageSchema).all()

def create_village(db: Session, req: CreateVillage):
    village = db.query(VillageSchema).filter(VillageSchema.name == req.name).first()
    if village:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Village {req.name} already exists!"
        )
    new_village = VillageSchema(
        id = uuid4(),
        name = req.name,
        description = req.description,
        chief = req.chief,
        country = req.country
    )
    db.add(new_village)
    db.commit()
    db.refresh(new_village)
    return new_village
