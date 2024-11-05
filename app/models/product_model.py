from beanie import Document, PydanticObjectId
from typing import List, Optional

from fastapi import HTTPException

from app.schemas.product_report_schema import ProductReportSchema
from app.schemas.year_schema import Year
from app.utils.report_generator import ReportGenerator

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
            # Filtering the most recent available year
            selected_year = max(
                (year for year in product.years 
                 if specific_year is None or year.year == specific_year),
                key=lambda y: y.year,
                default=None
            )
            
            if selected_year is None:
                continue  # Skip the product if the desired year is not found
            
            product_data = product.model_dump()
            product_data["value"] = selected_year.value  # Replace `years` with `year`
            del product_data["years"] # Remove the `years` field
            del product_data["id"]  # Remove the `id` field
            result.append(product_data)

        
        
        if not result:
            raise HTTPException(status_code=404, detail="No products found for the given type or year")
        
        return ReportGenerator(result, year=specific_year, type=type_value).create_product_report()

    
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

