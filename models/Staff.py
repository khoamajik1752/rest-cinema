from pydantic import BaseModel
from datetime import datetime

    
class Staff(BaseModel):
    Username: str
    Password: str
    Email: str
    Tel:str
    Role:list[str]
    Created_time:datetime
    Updated_time:datetime
    Last_login:datetime