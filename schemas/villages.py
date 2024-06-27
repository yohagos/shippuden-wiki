from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from database.db import Base

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Village(Base):
    __tablename__ = "villages"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    country = Column(String)
    chief = Column(String, unique=True)
    
    