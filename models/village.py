from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class Village(BaseModel):
    id: UUID
    name: str
    description: Optional[str]  = None
    country: str
    chief: str

class ShowVillage(Village):
    class Config():
        from_attributes = True

class CreateVillage(BaseModel):
    name: str
    description: Optional[str]  = None
    country: str
    chief: str