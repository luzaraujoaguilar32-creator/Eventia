from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from backend.config import settings

# PostgreSQL: usuarios, roles y suscripciones.
pg_engine = create_engine(settings.postgres_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=pg_engine, autoflush=False, autocommit=False)

# MongoDB: información operativa de eventos.
mongo_client = MongoClient(settings.mongodb_url)
mongo_db = mongo_client[settings.mongodb_database]

def get_pg_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
