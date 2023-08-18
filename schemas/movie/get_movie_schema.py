from .movie_schema import movie_full_schema
from pydantic import BaseModel

class movie_get_request(BaseModel):
    name:str

class movie_get_response(movie_full_schema):
    pass
    