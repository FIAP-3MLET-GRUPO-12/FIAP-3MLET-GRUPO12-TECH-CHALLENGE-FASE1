from typing import List, Optional
from beanie import Document, PydanticObjectId
from pydantic import BaseModel


class Trade(Document):
    id: Optional[PydanticObjectId] = None
    country: str
    category: str
    type: str
    years: List["TradeYear"] = []

    class Settings:
        collection = "trade"
    
    class Config:
         json_schema_extra = {
            "example": {
                "country": "Country Name",
                "category": "Category Name",
                "type": "Type Name",
                "years": [
                    {
                        "year": 2021,
                        "value": 100,
                        "qtd": 10
                    }
                ]
            }
         }


class TradeYear(BaseModel):
    year: int
    value: int
    qtd: int
