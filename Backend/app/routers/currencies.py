from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from ..database import SessionLocal
from ..models import CurrencyRate
from ..schemas import CurrencyRateResponse
from ..services.nbp_service import fetch_rates_from_nbp

router = APIRouter(prefix="/currencies", tags=["Currencies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[str])
def get_available_currencies(db: Session = Depends(get_db)):
    currencies = db.query(CurrencyRate.currency).distinct().all()
    return [c[0] for c in currencies]


@router.get("/{rate_date}", response_model=list[CurrencyRateResponse])
def get_rates_by_date(rate_date: date, db: Session = Depends(get_db)):
    rates = db.query(CurrencyRate).filter(CurrencyRate.date == rate_date).all()
    if not rates:
        raise HTTPException(status_code=404, detail="No data for this date")
    return rates


@router.post("/fetch")
def fetch_and_save_rates(db: Session = Depends(get_db)):
    rates = fetch_rates_from_nbp()

    for rate in rates:
        exists = db.query(CurrencyRate).filter(
            CurrencyRate.currency == rate["currency"],
            CurrencyRate.date == rate["date"]
        ).first()

        if not exists:
            db.add(CurrencyRate(**rate))

    db.commit()
    return {"message": "Rates fetched and saved"}
