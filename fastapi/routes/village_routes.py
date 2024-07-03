from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from database.db import get_db
from schemas.village import ShowVillage, CreateVillage
from schemas.page_response import PaginationResponse
from services.village_service import all_villages, create_village, get_village_by_id


router = APIRouter(
    prefix="/village",
    tags=["Villages"],
)

@router.get('s', response_model=PaginationResponse)
def get_villages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return all_villages(skip, limit, db)

@router.get('/{village_id}')
def get_village(village_id: UUID, db: Session = Depends(get_db)):
    return get_village_by_id(village_id, db)

@router.post('', response_model=ShowVillage)
async def add_village(village_req: CreateVillage, db: Session = Depends(get_db)):
    return create_village(db, village_req)


