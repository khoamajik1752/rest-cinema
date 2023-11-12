from typing import Annotated, Union
from fastapi import Form
from pydantic import BaseModel


class loginResponse(BaseModel):
    
    access_token:str
    username: str
    email: str | None = None
    full_name: str | None = None
    user_id:str
    roles:list[str]

class UserLogin(BaseModel):
    username: str
    password: str