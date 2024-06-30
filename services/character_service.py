from fastapi import status, HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from uuid import uuid4

from schemas.characters import Character
from models.character import CharacterCreate


def all_characters(db: Session):
    return db.query(Character).all()

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
