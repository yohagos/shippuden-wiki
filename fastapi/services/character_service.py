from fastapi import status, HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from uuid import uuid4, UUID
from base64 import b64encode

from models.characters import Character
from schemas.character import CharacterCreate, ShowCharacters
from schemas.image_file import ShowImageFile
from schemas.page_response import PaginationMeta, PaginationResponse

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def all_characters(skip: int, limit: int, db: Session):
    total_items = db.query(Character).count()
    total_pages = (total_items + limit - 1) // limit
    current_page = (skip // limit) + 1
    characters = db.query(Character).offset(skip).limit(limit).all()

    character_data = [
        ShowCharacters(
            id=char.id,
            fullname=char.fullname,
            firstname=char.firstname,
            lastname=char.lastname,
            gender=char.gender,
            age=char.age,
            is_alive=char.is_alive,
            images=[
                ShowImageFile(
                    id=img.id,
                    filename=img.filename,
                    content=b64encode(img.content).decode("utf-8"),
                    content_type=img.content_type
                ) for img in char.images
            ]
        ) for char in characters
    ]

    return PaginationResponse(
        data=character_data,
        meta=PaginationMeta(
            total_items=total_items,
            total_pages=total_pages,
            current_page=current_page,
            page_size=limit
        )
    )



def get_character_by_id(character_id: UUID, db: Session):
    return db.query(Character).filter(Character.id == character_id).first()

def save_character(character: CharacterCreate, db: Session):
    new_character = db.query(Character).filter(and_(Character.firstname == character.firstname, Character.lastname == character.lastname)).first()
    if new_character:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Character with name {character.firstname} {character.lastname} already exists")
    new_character = Character(
        id=uuid4(),
        firstname=character.firstname,
        lastname=character.lastname,
        fullname=character.lastname + " " + character.firstname,
        age=character.age,
        is_alive= character.is_alive,
        gender=character.gender
    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return new_character
