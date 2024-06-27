from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.character import Character

from utils.examples import characters

router = APIRouter(
    prefix="/characters",
    tags=["Characters"],
)

@router.get('', response_model=List[Character])
def get_characters():
    return characters