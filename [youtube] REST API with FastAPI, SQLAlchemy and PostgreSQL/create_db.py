from database import Base, engige
from models import Item

print("Creating satabase ...")

Base.metadata.create_all(engige)