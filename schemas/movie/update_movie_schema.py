from .movie_schema import movie_full_schema
from pydantic import BaseModel

class movie_update_request(BaseModel):
    id:str
    Name:str
    Author:str
    Description:str


class movie_update_response(movie_full_schema):
    pass
    