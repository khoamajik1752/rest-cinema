from .food_schema import food_service_full_schema
from pydantic import BaseModel

class food_service_update_request(BaseModel):
    id:str
    Name:str
    Price:float
    
class food_service_update_response(food_service_full_schema):
    pass