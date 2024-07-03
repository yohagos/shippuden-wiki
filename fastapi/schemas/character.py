from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID

from .image_file import ShowImageFile

class Character(BaseModel):
    id: UUID
    firstname: str
    lastname: str
    fullname: str
    age: Optional[int] = None
    gender: Optional[str] = None
    is_alive: Optional[bool] = None
    

class CharacterCreate(BaseModel):
    firstname: str
    lastname: str
    age: Optional[int] = None
    gender: Optional[str] = None
    is_alive: Optional[bool] = None

class ShowCharacters(Character):
    images: Optional[List[ShowImageFile]] = []

    class Config():
        from_attributes = True

class ShowBaseCharacter(Character):

    class Config():
        from_attributes = True