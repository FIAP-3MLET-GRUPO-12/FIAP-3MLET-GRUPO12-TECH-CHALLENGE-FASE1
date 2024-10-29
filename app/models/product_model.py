from beanie import Document
from pydantic import BaseModel
from typing import List

class Product(Document):
    id: str
    name: str
    category: str
    type: str
    years: List["Year"]

    class Settings:
        collection = "products"

class Year(BaseModel):
    year: int
    value: int