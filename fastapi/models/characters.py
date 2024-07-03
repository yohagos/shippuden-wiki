from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    fullname = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_alive = Column(Boolean, default=True)
    
    images = relationship(
        "ImageFile", 
        back_populates="character"
    )