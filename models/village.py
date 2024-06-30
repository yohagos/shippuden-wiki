from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from .image_file import ShowImageFile

class Village(BaseModel):
    id: UUID
    name: str
    description: Optional[str]  = None
    country: str
    chief: str

class ShowVillage(Village):
    images: Optional[List[ShowImageFile]] = []
    class Config():
        from_attributes = True

class CreateVillage(BaseModel):
    name: str
    description: Optional[str]  = None
    country: str
    chief: str
    