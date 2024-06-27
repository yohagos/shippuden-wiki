from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Character(Base):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    fullname = Column(String)
    age = Column(Integer)
    gender = Column(String)
    is_alive = Column(Boolean, default=True)
    