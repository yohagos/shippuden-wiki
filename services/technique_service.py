from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from schemas.techniques import Technique

def all_techniques(db: Session):
    return db.query(Technique).all()

