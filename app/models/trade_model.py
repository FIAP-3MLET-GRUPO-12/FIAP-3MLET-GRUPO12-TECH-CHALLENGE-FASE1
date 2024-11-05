from typing import List, Optional
from beanie import Document, PydanticObjectId
from fastapi import HTTPException
from pydantic import BaseModel

from app.utils.report_generator import ReportGenerator


class Trade(Document):
    id: Optional[PydanticObjectId] = None
    country: str
    category: str
    type: str
    years: List["TradeYear"] = []

    class Settings:
        collection = "trade"
        
    @classmethod
    async def find_by_derivative_with_year(
        cls, 
        type_value: str,
        derivative: str,
        specific_year: Optional[int] = None
    ) -> List[dict]:
        trades = await cls.find((cls.category == derivative) and (cls.type == type_value)).to_list()
        
        result = []
        for trade in trades:
            # Filtering the most recent available year
            selected_year = max(
                (year for year in trade.years 
                 if specific_year is None or year.year == specific_year),
                key=lambda y: y.year,
                default=None
            )
            
            if selected_year is None:
                continue  # Skip the trade if the desired year is not found
            
            trade_data = trade.model_dump()
            trade_data["year_value"] = selected_year
            del trade_data["years"]
            del trade_data["id"]
            result.append(trade_data)
        
        if not result:
            raise HTTPException(status_code=404, detail="No trades found for the given type or year")
        
        return ReportGenerator(result, year=specific_year, type=type_value).create_trade_report(derivative=derivative, type=type_value, trades=result)
    
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
