from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Any


class ImageFileBase(BaseModel):
    filename: str
    content: bytes
    content_type: str
    village_id: Optional[UUID] = None
    village: Optional[Any] = None
    character_id: Optional[UUID] = None
    character: Optional[Any] = None
    technique_id: Optional[UUID] = None
    technique: Optional[Any] = None

class ImageFile(ImageFileBase):
    id: UUID

class ShowImageFile(ImageFile):
    class Config():
        from_attributes=True

