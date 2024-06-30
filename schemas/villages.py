from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base


class Village(Base):
    __tablename__ = "villages"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    country = Column(String)
    chief = Column(String, unique=True)
    
    images = relationship(
        "ImageFile", 
        back_populates="village", 
        primaryjoin="and_(Village.id == foreign(ImageFile.village_id))"
    )
    