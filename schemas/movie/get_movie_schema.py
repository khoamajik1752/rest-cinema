from .movie_schema import movie_full_schema
from pydantic import BaseModel,Field
from typing import Optional
class movie_get_request(movie_full_schema):
    Name: Optional[str]=None
    Author:  Optional[str]=None
    Description: Optional[str]=None
    
class movie_get_schema_mapping(BaseModel):
    Name: str 
    Author:str 
    Description:str

class movie_get_response(movie_full_schema):
    pass
    