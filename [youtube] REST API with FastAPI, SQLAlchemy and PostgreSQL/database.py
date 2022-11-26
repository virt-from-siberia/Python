from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://localhost:5432/template1"

engige = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


Base = declarative_base()

SessionLocal = sessionmaker(bind=engige)
