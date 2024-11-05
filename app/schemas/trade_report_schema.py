

from pydantic import BaseModel


class TradeReportSchema(BaseModel):
    derivative: str
    year: int
    type: str
    trades: list["TradeReportItemSchema"]
        
class TradeReportItemSchema(BaseModel):
    country: str
    quantity: int
    value: int