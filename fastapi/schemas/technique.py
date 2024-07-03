from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID
from enum import Enum

from .image_file import ShowImageFile

class TechniqueTypes(Enum): 
    TAIJUTSU = "Taijutsu"
    NINJUTSU = "Ninjutsu"
    GENJUTSU = "Genjutsu"

class NatureTypes(Enum):
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth"
    WIND = "Wind"
    LIGHTNING = "Lightning"
    ICE = "Ice"
    LIGHT = "Light"
    DARKNESS = "Darkness"
    WOOD = "Wood"
    LAVA = "Lava"
    POISON = "Poison"

class TechniqueCreate(BaseModel):
    name: str
    description: str
    clan: Optional[str] = None
    kekkai_genkai: Optional[str] = None

class ShowBaseTechniques(BaseModel):
    id: UUID
    name: str
    description: str
    technique_type: TechniqueTypes
    nature_type: Optional[NatureTypes] = None

    class Config():
        from_attributes = True


class Technique(BaseModel):
    id: UUID
    name: str
    description: str
    technique_type: TechniqueTypes
    nature_type: Optional[NatureTypes] = None
    kekkai_genkai: Optional[str] = None
    clan: Optional[str] = None
    images: Optional[List[ShowImageFile]] = []

class ShowTechniques(Technique):
    class Config():
        from_attributes = True
        #orm_mode = True
