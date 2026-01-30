from pytest_bdd import scenarios, given, when, then
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import CurrencyRate
from datetime import date

client = TestClient(app)
scenarios('../features/currency.feature')

# -----------------------------
# GIVEN
# -----------------------------
@given("the API is running")
def api_running():
    response = client.get("/")
    assert response.status_code == 200

@given("currency rates are fetched")
def currency_fetched():
    response = client.post("/currencies/fetch")
    assert response.status_code == 200

@given("the database is available")
def db_available():
    try:
        db = SessionLocal()
        db.query(CurrencyRate).first()
    except Exception as e:
        assert False, f"DB connection failed: {e}"
    finally:
        db.close()

# -----------------------------
# WHEN
# -----------------------------
@when("I visit the root endpoint")
def visit_root():
    return client.get("/")

@when("I fetch currency rates")
def fetch_rates():
    return client.post("/currencies/fetch")

@when("I request the list of currencies")
def request_currencies():
    return client.get("/currencies/")

@when("I request rates for the first available date")
def request_rates_by_date():
    db = SessionLocal()
    first_rate = db.query(CurrencyRate).first()
    db.close()
    date = first_rate.date.strftime("%Y-%m-%d")
    return client.get(f"/currencies/{date}")

# -----------------------------
# THEN
# -----------------------------
@then('I should receive a status 200 and message "API is running"')
def check_root_response():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

@then('the response should confirm "Rates fetched and saved"')
def check_fetch_response():
    response = client.post("/currencies/fetch")
    data = response.json()
    assert "message" in data
    assert data["message"] == "Rates fetched and saved"

@then('I should receive a non-empty list containing "USD" or "EUR"')
def check_currencies_list():
    response = client.get("/currencies/")
    data = response.json()
    assert isinstance(data, list)
    assert "USD" in data or "EUR" in data

@then("I should receive a list of rates with correct currency, rate and date")
def check_rates_by_date():
    db = SessionLocal()
    first_rate = db.query(CurrencyRate).first()
    db.close()
    date = first_rate.date.strftime("%Y-%m-%d")

    response = client.get(f"/currencies/{date}")
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "currency" in item
        assert "rate" in item
        assert "date" in item
        assert item["date"] == date

@then("I should be able to query CurrencyRate without errors")
def check_db_connection():
    try:
        db = SessionLocal()
        db.query(CurrencyRate).first()
    finally:
        db.close()

@then("all rates should have valid currency, rate > 0, and valid date")
def check_data_integrity():
    db = SessionLocal()
    rates = db.query(CurrencyRate).all()
    db.close()

    assert len(rates) > 0, "No currency rates in database"
    for rate in rates:
        assert isinstance(rate.currency, str)
        assert isinstance(rate.rate, float)
        assert isinstance(rate.date, date)
        assert rate.rate > 0, f"Invalid rate for {rate.currency}"
