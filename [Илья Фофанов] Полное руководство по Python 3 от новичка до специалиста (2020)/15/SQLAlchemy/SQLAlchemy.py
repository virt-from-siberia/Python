import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgre@localhost:5432/testDB')
connection = engine.connect()

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    rating = Column(Float)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# author = Author(author_id=19, full_name='Mike Taishon', rating=4.5)
# session.add(author)
# session.commit()

# for item in session.query(Author).order_by(Author.rating):
#     print(item.full_name, ' ', item.rating)

for item in session.query(Author).filter(Author.rating > 4.5):
    print(item.full_name, ' ', item.rating)
