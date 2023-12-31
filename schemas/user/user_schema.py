from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId

class user_full_schema(BaseModel):
    _id:str
    Username: str
    Password: str
    Fullname:str
    Email: str
    Tel:str
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime
    
class user_without_password_schema(BaseModel):
    _id:ObjectId
    Username: str
    Fullname:str
    Email: str
    Tel:str
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime
    