from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.technique import Technique

from utils.examples import techniques

router = APIRouter(
    prefix="/techniques",
    tags=["Techniques"],
)

@router.get('', response_model=List[Technique])
def get_techniques():
    return techniques