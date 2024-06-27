from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class Character(BaseModel):
    id: UUID
    firstname: str
    lastname: str
    fullname: str
    age: Optional[int] = None
    gender: Optional[str] = None
    is_alive: Optional[bool] = None

class CharacterCreate(Character):
    pass