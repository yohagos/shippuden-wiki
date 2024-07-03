from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from database.db import get_db
from schemas.page_response import PaginationResponse
from schemas.technique import ShowTechniques, TechniqueCreate, NatureTypes, TechniqueTypes
from services.technique_service import all_techniques, add_technique, get_technique_by_id

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/technique",
    tags=["Techniques"],
)

@router.get('s', response_model=PaginationResponse)
def get_techniques(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return all_techniques(skip, limit, db)

@router.get('/{technique_id}')
def get_technique(technique_id: UUID, db: Session = Depends(get_db)):
    return get_technique_by_id(technique_id, db)

@router.post('', response_model=ShowTechniques)
def create_technique(technique: TechniqueCreate, techniqueType: TechniqueTypes, naturalTypes: NatureTypes = None, db: Session = Depends(get_db)):
    return add_technique(technique, techniqueType, naturalTypes, db)
