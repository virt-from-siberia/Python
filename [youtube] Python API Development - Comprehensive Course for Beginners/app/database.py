from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/pythonApiDevelopment'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='pythonApiDevelopment',
#             user='postgres', password='postgres',
#             cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected to PostgreSQL was successful")
#         break
#     except Exception as error:
#         print('Could not connect to PostgreSQL')
#         print("error: ", error)
#         time.sleep(2)
