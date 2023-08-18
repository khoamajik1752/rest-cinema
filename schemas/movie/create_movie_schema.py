from .movie_schema import movie_full_schema
from pydantic import BaseModel

class movie_create_request(BaseModel):
    Name:str
    Author:str
    Description:str

class movie_create_response(movie_full_schema):
    pass
    