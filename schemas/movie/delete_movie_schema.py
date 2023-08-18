from .movie_schema import movie_full_schema
from pydantic import BaseModel
class movie_delete_request(BaseModel):
    id:str

class movie_delete_response(movie_full_schema):
    pass
    