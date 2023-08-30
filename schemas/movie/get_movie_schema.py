from .movie_schema import movie_full_schema
from pydantic import BaseModel,Field

class movie_get_request(movie_full_schema):
    Name: str = Field(None)
    Author: str = Field(None)
    Description: str = Field(None)
    
class movie_get_schema_mapping(BaseModel):
    Name: str = Field(default={"$exists":True})
    Author:str = Field(default={"$exists":True})
    Description:str = Field(default={"$exists":True})

class movie_get_response(movie_full_schema):
    pass
    