from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4, UUID
from base64 import b64encode

from models.techniques import Technique
from schemas.technique import TechniqueCreate, NatureTypes, TechniqueTypes, ShowTechniques
from schemas.page_response import PaginationMeta, PaginationResponse
from schemas.image_file import ShowImageFile

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def all_techniques(skip: int, limit: int, db: Session):
    total_items = db.query(Technique).count()
    total_pages = (total_items + limit - 1) // limit
    current_page = (skip // limit) + 1
    techs = db.query(Technique).offset(skip).limit(limit).all()
    
    techniques_data = [
        ShowTechniques(
            id=t.id,
            name=t.name,
            description=t.description,
            technique_type=t.technique_type,
            nature_type=t.nature_type,
            kekkai_genkai=t.kekkai_genkai,
            clan=t.clan,
            images=[
                ShowImageFile(
                    id=img.id,
                    filename=img.filename,
                    content=b64encode(img.content).decode("utf-8"),
                    content_type=img.content_type,
                    technique_id=t.id
                ) for img in t.images
            ] 
        ) for t in techs
    ]
    return PaginationResponse(
        data=techniques_data,
        meta=PaginationMeta(
            total_items=total_items,
            total_pages=total_pages,
            current_page=current_page,
            page_size=limit
        )
    )

def get_technique_by_id(technique_id: UUID, db:Session):
    return db.query(Technique).filter(Technique.id == technique_id).first()

def add_technique(
        tech: TechniqueCreate,
        techType: TechniqueTypes,
        nature: NatureTypes,
        db: Session
):
    new_technique = db.query(Technique).filter(Technique.name == tech.name).first()
    if new_technique:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Technique {tech.name} already exists")
    if techType.value not in [e.value for e in TechniqueTypes]:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Technique Type {techType._value_} cannot be recognized")
    if nature is not None and nature.value not in [e.value for e in NatureTypes]:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Nature Type {nature._value_} cannot be recognized")
    new_technique = Technique(
        id=uuid4(),
        name=tech.name,
        description=tech.description,
        technique_type=techType.value,
        nature_type=nature.value if nature is not None else None,
        clan=tech.clan if tech.clan is not None and len(tech.clan) > 0 else None,
        kekkai_genkai=tech.kekkai_genkai
    )
    db.add(new_technique)
    db.commit()
    db.refresh(new_technique)
    return new_technique