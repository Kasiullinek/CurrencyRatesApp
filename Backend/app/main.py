from fastapi import FastAPI
from .database import Base, engine
from .routers import currencies

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Currency Rates API")

app.include_router(currencies.router)

@app.get("/")
def root():
    return {"status": "API is running"}
