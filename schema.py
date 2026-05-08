from pydantic import BaseModel # pydantic is a data validation and settings management library that uses Python type annotations to validate and serialize data. It is commonly used in FastAPI to define request and response models, ensuring that the data sent to and from the API adheres to the specified structure and types.
from typing import Optional # Optional is used to indicate that a field can be of a certain type or None. It is commonly used in FastAPI to define optional fields in request and response models, allowing for more flexible data structures.

class ProductBase(BaseModel): # ProductBase is a Pydantic model that defines the common attributes for a product, such as name, description, price, and quantity. This model can be used as a base class for other models that represent different operations on products, such as creating a new product or updating an existing product. By using a base model, we can avoid code duplication and ensure consistency in the data structure across different operations.
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase): # ProductCreate is a Pydantic model that inherits from ProductBase and is used to define the attributes required for creating a new product. Since it inherits from ProductBase, it includes all the fields defined in ProductBase (name, description, price, quantity) and can be used to validate the request body data when creating a new product through the API. This model ensures that all the necessary information for creating a product is provided in the request.
    pass

class ProductUpdatePartail(BaseModel): # ProductUpdatePartail is a Pydantic model that defines the attributes for updating a product. All the fields in this model are optional, which allows us to perform partial updates on a product. When we use this model in a PATCH endpoint, we can update only the fields that are provided in the request body, while keeping the other fields unchanged. This is useful for scenarios where we want to update only a subset of the product's attributes without having to send the entire product data in the request.
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class ProductResponse(ProductBase): # ProductResponse is a Pydantic model that inherits from ProductBase and adds an additional field id, which represents the unique identifier of the product. This model is used to define the structure of the response data when retrieving product information from the API. By including the id field, we can provide clients with the necessary information to identify and reference specific products in subsequent API calls.
    id: int

    class Config: # The Config class is a special inner class in Pydantic models that allows us to configure various settings for the model. In this case, we set orm_mode = True, which tells Pydantic to treat the model as an ORM (Object-Relational Mapping) model. This means that when we return a SQLAlchemy model instance from our API endpoints, Pydantic will be able to convert it into the appropriate response format defined by the ProductResponse model. This is particularly useful when working with SQLAlchemy models, as it allows us to seamlessly integrate our database models with our API response models.

        from_attributes = True # orm_model is renamed to from_attributes in Pydantic v2. This setting allows Pydantic to create model instances from ORM objects by reading their attributes, which is essential for integrating SQLAlchemy models with Pydantic response models in FastAPI.

class ProductAPIResponse(BaseModel): # ProductAPIResponse is a Pydantic model that defines the structure of the API response when performing operations on products, such as creating, updating, or deleting a product. It includes fields for status, status_code, message, and product. The status field indicates whether the operation was successful or not, the status_code field provides the HTTP status code for the response, the message field contains a descriptive message about the operation, and the product field contains the details of the product involved in the operation, represented by the ProductResponse model. This model helps to standardize the API responses and provide clear information to clients about the outcome of their requests.
    status: str
    status_code: int
    message: str
    product: ProductResponse