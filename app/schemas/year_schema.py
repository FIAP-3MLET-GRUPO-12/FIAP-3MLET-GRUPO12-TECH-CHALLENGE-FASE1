from pydantic import BaseModel


class Year(BaseModel):
    year: int
    value: int