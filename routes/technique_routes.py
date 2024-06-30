from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.technique import ShowTechniques
from services.technique_service import all_techniques


router = APIRouter(
    prefix="/techniques",
    tags=["Techniques"],
)

@router.get('', response_model=List[ShowTechniques])
def get_techniques(db: Session = Depends(get_db)):
    return all_techniques(db)