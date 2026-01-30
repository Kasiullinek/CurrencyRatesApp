from datetime import date
from pydantic import BaseModel
from pydantic import ConfigDict

class CurrencyRateBase(BaseModel):
    currency: str
    rate: float
    date: date

class CurrencyRateResponse(CurrencyRateBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
