from .food_schema import food_service_full_schema
from pydantic import BaseModel
class food_service_get_request(BaseModel):
    Name:str

class food_service_get_response(food_service_full_schema):
    pass
    