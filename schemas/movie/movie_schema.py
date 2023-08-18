from pydantic import BaseModel 

class movie_full_schema(BaseModel):
    Name:str
    Author:str
    Description:str