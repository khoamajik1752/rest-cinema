from pydantic import BaseModel


class loginResponse(BaseModel):
    access_token:str

class UserLogin(BaseModel):
    username: str
    password: str