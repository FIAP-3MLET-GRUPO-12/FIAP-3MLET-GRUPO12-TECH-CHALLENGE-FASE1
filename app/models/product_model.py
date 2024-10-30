from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import List, Optional

class Product(Document):
    id: Optional[PydanticObjectId] = None
    name: str
    category: str
    type: str
    years: List["Year"] = []

    class Settings:
        collection = "products"
    
    class Config:
         json_schema_extra = {
            "example": {
                "name": "Product Name",
                "category": "Category Name",
                "type": "Type Name",
                "years": [
                    {
                        "year": 2021,
                        "value": 100
                    }
                ]
            }
         }

class Year(BaseModel):
    year: int
    value: int