from enum import Enum
from sqlalchemy import Column, String, Boolean, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, ENUM

from database.db import Base

class TechniqueTypes(str, Enum): 
    TAIJUTSU = "Taijutsu"
    NINJUTSU = "Ninjutsu"
    GENJUTSU = "Genjutsu"

class NatureTypes(str, Enum):
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
    

class Technique(Base):
    __tablename__ = "techniques"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    technique_type = Column(ENUM(TechniqueTypes), nullable=False)
    nature_type = Column(ENUM(NatureTypes))
    kekkai_genkai = Column(Boolean)
    clan = Column(String)
    description = Column(String)

    images = relationship(
        "ImageFile", 
        back_populates="technique"
    )