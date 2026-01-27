from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import currencies

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Currency Rates API")

origins = [
    "http://localhost:4200", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)

app.include_router(currencies.router)

@app.get("/")
def root():
    return {"status": "API is running"}
