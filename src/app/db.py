from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://app_user:app_password@db/app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
