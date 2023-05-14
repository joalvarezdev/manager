from sqlalchemy import Column, Integer, String, Float
from config.database import base


class Product(base):
    __tablename__: str = "products"

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)
