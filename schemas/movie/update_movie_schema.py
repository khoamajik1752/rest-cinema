import pydantic 
from pydantic import basemodel
class update_movie_request(basemodel):
    id:int
    title:str

class update_movie_response(basemodel):
    id:int
    