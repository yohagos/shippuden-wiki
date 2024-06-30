from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from models.image_file import ImageFile

def create_image_file(
        file: ImageFile,
        db: Session
):
    db.add(file)
    db.commit()
    db.refresh(file)
    return file