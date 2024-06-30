from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.character import ShowCharacters, CharacterCreate
from services.character_service import all_characters, save_character

router = APIRouter(
    prefix="/characters",
    tags=["Characters"],
)

@router.get('s', response_model=List[ShowCharacters])
def get_characters(db: Session = Depends(get_db)):
    return all_characters(db)

@router.post('', response_model=ShowCharacters)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    return save_character(character, db)