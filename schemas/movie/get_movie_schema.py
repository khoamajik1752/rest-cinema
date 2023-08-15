
from pydantic import BaseModel
class get_movie_request(BaseModel):
    id:int
    title:str

class get_movie_response(BaseModel):
    id:int
    