from pydantic import BaseModel
from datetime import datetime
from .user_schema import user_full_schema,user_without_password_schema

class user_get_information_request(BaseModel):
    id:str
    
class user_get_information_response(user_without_password_schema):
    pass
    
class user_get_with_password_response(user_full_schema):
    pass
    