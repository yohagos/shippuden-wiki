from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from database.db import get_db
from schemas.page_response import PaginationResponse
from schemas.character import ShowCharacters, CharacterCreate
from services.character_service import all_characters, save_character, get_character_by_id

router = APIRouter(
    prefix="/character",
    tags=["Characters"],
)

@router.get('s', response_model=PaginationResponse)
def get_characters(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return all_characters(skip, limit, db)

@router.get('/{character_id}')
def get_character(character_id: UUID, db: Session = Depends(get_db)):
    return get_character_by_id(character_id, db)

@router.post('', response_model=ShowCharacters)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    return save_character(character, db)