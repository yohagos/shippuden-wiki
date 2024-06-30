from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.village import ShowVillage, CreateVillage
from services.village_service import all_villages, create_village


router = APIRouter(
    prefix="/village",
    tags=["Villages"],
)

@router.get('s', response_model=List[ShowVillage])
def get_villages(db: Session = Depends(get_db)):
    return all_villages(db)

@router.post('', response_model=ShowVillage)
async def add_village(village_req: CreateVillage, db: Session = Depends(get_db)):
    return create_village(db, village_req)

