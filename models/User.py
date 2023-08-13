from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    Username: str
    Password: str
    Email: str
    Tel:str
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime



