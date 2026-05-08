from fastapi import FastAPI, HTTPException, status , Depends
from models import Product
from database import db_session, engine, Base, get_db
from schema import ProductCreate, ProductAPIResponse, ProductUpdatePartail, ProductsAPIResponse
from sqlalchemy.orm import Session  #type: ignore
from localdb import products
import os

Base.metadata.create_all(bind=engine) # create the tables in the database if they don't exist

app = FastAPI() # create a FastAPI instance
    
# Initialize the database with the products from the localdb if the database is empty
def init_db():
    db = db_session() # depends(get_db) only work inside the route handlers, so we have to create a db session manually here
    if db.query(Product).count() == 0: # if there are no products in the database, then we will add the products from the localdb
        for product in products:
            db.add(product) # add the product to the database session
        db.commit()
init_db() # initialize the database with the products from the localdb if the database is empty

# health check endpoint 
@app.get("/health", status_code=status.HTTP_200_OK) # status_code = (The default status code to be used for the response. It can be overridden in the route handler if needed.)
def health_check():
    return {
        "status": "success",
        "status_code": 200,
        "message": "Server is running"
    }

# CRUD endpoints for products
@app.get("/product", status_code=status.HTTP_200_OK, response_model=ProductsAPIResponse) # response_model = (The model to use for the response. It can be used to validate and serialize the response data.)
def get_products(db: Session = Depends(get_db)): # Depends(get_db) is used to get a database session for the route handler. It will automatically close the database session after the request is finished.
    products = db.query(Product).all() # query the database to get all the products

    return {
        "status": "success",
        "status_code": 200,
        "message": "All products fetched successfully",
        "products": products
    }

# Get a single product by id
@app.get("/product/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductAPIResponse) # response_model = (The model to ... response data.)
def get_product(product_id: int, db: Session = Depends(get_db)): 
    product = db.query(Product).filter(Product.id == product_id).first() # query the database to get the product with the given id. first() is used to get the first result of the query, which is the product with the given id. If there is no product with the given id, then it will return None.
    if not product:
        raise HTTPException( # HTTPException is used to raise an exception with a specific status code and detail message. In this case, we are raising a 404 Not Found exception if the product with the given id is not found in the database.
            status_code=404,
            detail="Product not found"
        )

    return {
        "status": "success",
        "status_code": 200,
        "message": "Product fetched successfully",
        "product": product
    }

# Create a new product
@app.post("/product", status_code=status.HTTP_201_CREATED, response_model=ProductAPIResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)): # product: ProductCreate is used to validate the request body data against the ProductCreate model. If the request body data is not valid, then it will raise a 422 Unprocessable Entity exception.
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )
    db.add(new_product) # add the new product to the database session
    db.commit() # commit the changes to the database to save the new product
    db.refresh(new_product) # refresh the new product instance to get the updated data from the database, including the generated id

    return {
        "status": "success",
        "status_code": 201,
        "message": "Product added successfully",
        "product": new_product
    }

# Update an existing product using put for full update (all fields are required in the request body) 
@app.put("/product/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductAPIResponse)
def update_product(product_id: int, updated_product: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    # Update the product attributes with the new values from the request body
    product.name = updated_product.name
    product.description = updated_product.description
    product.price = updated_product.price
    product.quantity = updated_product.quantity

    db.commit() # commit the changes to the database to save the updated product
    db.refresh(product) # refresh the product instance to get the updated data from the database

    return {
        "status": "success",
        "status_code": 200,
        "message": "Product updated successfully",
        "product": product
    }

# Update an existing product using patch for partial update (only the fields that are provided in the request body will be updated)
@app.patch("/product/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductAPIResponse)
def partial_update_product(product_id: int, updated_product: ProductUpdatePartail, db: Session = Depends(get_db)): # updated_product: ProductUpdatePartail is used to validate the request body data against the ProductUpdatePartail model. Since all the fields in the ProductUpdatePartail model are optional, it allows us to update only the fields that are provided in the request body, while keeping the other fields unchanged.
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    # Update the product attributes with the new values from the request body if they are provided
    if updated_product.name is not None:
        product.name = updated_product.name
    if updated_product.description is not None:
        product.description = updated_product.description
    if updated_product.price is not None:
        product.price = updated_product.price
    if updated_product.quantity is not None:
        product.quantity = updated_product.quantity

    db.commit() # commit the changes to the database to save the updated product
    db.refresh(product) # refresh the product instance to get the updated data from the database

    return {
        "status": "success",
        "status_code": 200,
        "message": "Product partially updated successfully",
        "product": product
    }


# Delete a product
@app.delete("/product/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductAPIResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product) # delete the product from the database session
    db.commit()

    return {
        "status": "success",
        "status_code": 200,
        "message": "Product deleted successfully",
        "product": product
    }

# Run the application using Uvicorn ASGI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", # "main" is the name of the Python file (without the .py extension) and "app" is the name of the FastAPI instance we created in this file.
        host= os.getenv("HOST", "127.0.0.1"), # The host address to bind the server to. "
        port= int(os.getenv("PORT", 3000)), # The port number to bind the server to. You can choose any available port number.
        reload=True # Enable auto-reload for development. This will automatically restart the server whenever you make changes to the code, which is useful during development. You can set it to False in production for better performance.
    )