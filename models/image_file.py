from pydantic import BaseModel
from uuid import UUID

class ImageFileBase(BaseModel):
    filename: str
    content: bytes
    content_type: str
    subject_id: UUID
    subject_type: str

class ImageFile(ImageFileBase):
    id: UUID

class ShowImageFile(ImageFile):
    class Config():
        from_attributes=True

