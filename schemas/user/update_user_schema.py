from .user_schema import user_without_password_schema
from pydantic import BaseModel,Field
from datetime import datetime

# class user_update_information(BaseModel):
#     Fullname:str
#     Email: str
#     Tel:str
    
# class user_update_information_request(user_update_information):
#     id:str
    
# class user_update_information_schema_mapping(user_update_information):
#     Updated_time:datetime = Field(default=datetime.now())
    
class user_update_information_request(BaseModel):
    id:str
    Fullname:str
    Email: str
    Tel:str
    
    
class user_update_information_schema_mapping(user_update_information_request):
    Updated_time:datetime = Field(default=datetime.now())

class user_update_information_response(user_without_password_schema):   
    pass 
    
class user_update_password_request(BaseModel):
    id:str
    oldPassword:str
    Password:str
    
class user_update_password_schema_mapping(BaseModel):
    Password:str
    Updated_time:datetime = Field(default=datetime.now())
    
class user_update_password_response(user_without_password_schema):
    pass

    
    