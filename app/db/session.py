from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=Session, autoflush=False, autocommit=False)
def get_session():
    with SessionLocal() as session:
        yield session
