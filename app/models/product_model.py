from beanie import Document, PydanticObjectId
from typing import List, Optional

from fastapi import HTTPException

from app.schemas.product_report_schema import ProductReportSchema
from app.schemas.year_schema import Year
from app.utils.product_report_generator import ProductReportGenerator

class Product(Document):
    id: Optional[PydanticObjectId] = None
    name: str
    category: str
    type: str
    years: List["Year"] = []

    class Settings:
        collection = "products"
        
    @classmethod
    async def find_by_type_with_year(
        cls, 
        type_value: str, 
        specific_year: Optional[int] = None
    ) -> List[dict]:
        products = await cls.find(cls.type == type_value).to_list()
        
        result = []
        for product in products:
            # Filtrando o ano mais recente disponível
            selected_year = max(
                (year for year in product.years 
                 if specific_year is None or year.year == specific_year),
                key=lambda y: y.year,
                default=None
            )
            
            if selected_year is None:
                continue  # Pula o produto se o ano desejado não for encontrado
            
            product_data = product.model_dump()
            product_data["value"] = selected_year.value  # Substitui `years` por `year`
            del product_data["years"]  # Remove o campo `years`
            del product_data["id"]  # Remove o campo `id`
            result.append(product_data)

        
        
        if not result:
            raise HTTPException(status_code=404, detail="No products found for the given type or year")
        
        return ProductReportGenerator(result, year=specific_year, type=type_value).generate()

    
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

