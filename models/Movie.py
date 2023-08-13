from pydantic import BaseModel


class Movie(BaseModel):
    Name:str
    Author:str
    Description:str