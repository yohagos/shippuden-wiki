from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from enum import Enum

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

class Technique(BaseModel):
    id: UUID
    name: str
    description: str
    techniqueType: TechniqueTypes
    natureType: Optional[NatureTypes] = None
    kekkaiGenkai: Optional[str] = None
    clan: Optional[str] = None
