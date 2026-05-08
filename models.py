from sqlalchemy import Column, Integer, String, Float # type: ignore
from database import Base

class Product(Base): # Product is a SQLAlchemy model that represents the products table in the database. It defines the columns and their data types for the products table, such as id, name, description, price, and quantity. This model is used to interact with the products table in the database, allowing us to perform CRUD operations on the products data through our API endpoints.
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False) # make sure of adding String(255) to specify the maximum length of the string, and nullable=False to ensure that the name field cannot be null in the database. Postgres will not complain for this if you leave String() without a length, but MySQL will throw an error. So it's a good practice to specify the length of the string when defining string columns in SQLAlchemy models, especially if you want to ensure compatibility with different database systems.
    description = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)