from typing import List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel

from app.schemas.year_schema import Year


class ProductSchema(BaseModel):
    id: Optional[PydanticObjectId] = None
    name: str
    category: str
    type: str
    years: List["Year"] = []