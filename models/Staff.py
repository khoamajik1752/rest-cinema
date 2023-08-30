from pydantic import BaseModel
from datetime import datetime
from .User import User

    
class Staff(User):
    Age: int
    Address:str
    Role:list[str]