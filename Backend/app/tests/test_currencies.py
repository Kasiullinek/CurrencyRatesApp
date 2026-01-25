from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import CurrencyRate
from datetime import datetime

client = TestClient(app)

# -----------------------------
# Test endpointów API
# -----------------------------

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_fetch_rates():
    response = client.post("/currencies/fetch")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Rates fetched and saved"

def test_get_currencies():
    client.post("/currencies/fetch")
    response = client.get("/currencies/")
    assert response.status_code == 200
    currencies = response.json()
    assert isinstance(currencies, list)
    assert "USD" in currencies or "EUR" in currencies

def test_get_rates_by_date():
    fetch_response = client.post("/currencies/fetch")
    
    db = SessionLocal()
    first_rate = db.query(CurrencyRate).first()
    db.close()
    rate_date = first_rate.date.strftime("%Y-%m-%d")

    response = client.get(f"/currencies/{rate_date}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "currency" in item
        assert "rate" in item
        assert "date" in item
        assert item["date"] == rate_date

# -----------------------------
# Testy połączenia z bazą danych
# -----------------------------

def test_db_connection():
    try:
        db = SessionLocal()
        db.query(CurrencyRate).first()
    except Exception as e:
        assert False, f"DB connection failed: {e}"
    finally:
        db.close()

# -----------------------------
# Testy poprawności danych
# -----------------------------

def test_data_integrity():
    client.post("/currencies/fetch")
    db = SessionLocal()
    rates = db.query(CurrencyRate).all()
    db.close()

    assert len(rates) > 0, "No currency rates in database"

    for rate in rates:
        assert isinstance(rate.currency, str)
        assert isinstance(rate.rate, float)
        assert isinstance(rate.date, datetime.date)
        assert rate.rate > 0, f"Invalid rate for {rate.currency}"
