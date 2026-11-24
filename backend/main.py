from fastapi import FastAPI
from backend.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "application": settings.app_name}

@app.get("/")
def root():
    return {"message": "API de Eventia", "docs": "/docs"}
