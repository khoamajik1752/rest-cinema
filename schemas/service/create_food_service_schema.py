from .food_schema import food_service_full_schema
from pydantic import BaseModel

class food_service_create_request(BaseModel):
    Name:str
    Price:float
    

class food_service_create_response(food_service_full_schema):
    pass
    