from datetime import date
from pydantic import BaseModel

class CurrencyRateBase(BaseModel):
    currency: str
    rate: float
    date: date

class CurrencyRateResponse(CurrencyRateBase):
    id: int

    class Config:
        from_attributes: True
