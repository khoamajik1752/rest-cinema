from .user_schema import user_without_password_schema
from pydantic import BaseModel
from datetime import datetime

class user_update_information_request(BaseModel):
    id:str
    Fullname:str
    Email: str
    Tel:str

class user_update_information_response(user_without_password_schema):   
    id:str
    pass 
    
class user_update_password_request(BaseModel):
    id:str
    oldPassword:str
    newPassword:str
    
class user_update_password_response(user_without_password_schema):
    id:str
    pass

    
    