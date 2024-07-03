from sqlalchemy import Column, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base

class ImageFile(Base):
    __tablename__ = 'image_files'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    filename=Column(String)
    content=Column(LargeBinary)
    content_type=Column(String)
    village_id = Column(UUID(as_uuid=True), ForeignKey('villages.id'), nullable=True)
    character_id = Column(UUID(as_uuid=True), ForeignKey('characters.id'), nullable=True)
    technique_id = Column(UUID(as_uuid=True), ForeignKey('techniques.id'), nullable=True)
    
    village = relationship("Village", back_populates="images")
    character = relationship("Character", back_populates="images")
    technique = relationship("Technique", back_populates="images")