from pydantic import BaseModel
from typing import List, Any

class PaginationMeta(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    page_size: int

class PaginationResponse(BaseModel):
    data: List[Any]
    meta: PaginationMeta
