from pydantic import BaseModel
from datetime import datetime

class user_full_schema(BaseModel):
    id:str
    Username: str
    Password: str
    Fullname:str
    Email: str
    Tel:str
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime
    
class user_without_password_schema(BaseModel):
    id:str
    Username: str
    Fullname:str
    Email: str
    Tel:str
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime
    