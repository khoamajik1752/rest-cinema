from .user_schema import user_without_password_schema,user_full_schema
from datetime import datetime
from pydantic import BaseModel,Field

class user_create_request(BaseModel):
    Username:str
    Password:str
    Fullname:str
    Email: str
    Tel:str
    
class user_create_schema_mapping(user_full_schema):
    Created_time:datetime = Field(default=datetime.now())
    Updated_time:datetime = Field(default=datetime.now())
    Last_login:datetime = Field(default=datetime.now())

class user_create_response(user_without_password_schema):
    pass
    