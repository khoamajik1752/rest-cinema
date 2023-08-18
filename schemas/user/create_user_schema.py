from .user_schema import user_without_password_schema
from pydantic import BaseModel

class user_create_request(BaseModel):
    Username:str
    Password:str
    Fullname:str
    Email: str
    Tel:str

class user_create_response(user_without_password_schema):
    id:str
    pass
    