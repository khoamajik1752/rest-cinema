from .food_schema import food_service_full_schema
from pydantic import BaseModel
class food_service_delete_request(BaseModel):
    id:str

class food_service_delete_response(food_service_full_schema):
    pass
    