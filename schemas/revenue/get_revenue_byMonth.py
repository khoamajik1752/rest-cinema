from .movie_schema import movie_full_schema
from pydantic import BaseModel

class revenue_month_get_request(BaseModel):
    Month: int
    Year: int

class revenue_moth_get_response(...):
    pass
    