from sqlalchemy import Column, Integer, String, Float # type: ignore
from database import Base

class Product(Base): # Product is a SQLAlchemy model that represents the products table in the database. It defines the columns and their data types for the products table, such as id, name, description, price, and quantity. This model is used to interact with the products table in the database, allowing us to perform CRUD operations on the products data through our API endpoints.
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)