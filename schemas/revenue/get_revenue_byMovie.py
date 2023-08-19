from .movie_schema import movie_full_schema
from pydantic import BaseModel

class revenue_movie_get_request(BaseModel):
    MovieID: string

class revenue_movie_get_response(...):
    pass
    