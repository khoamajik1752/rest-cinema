from datetime import time, datetime,timedelta
from pydantic import BaseModel 

class SearchMovieSchema(BaseModel):
    Name:str
    Datetime: datetime
    Movie_Screening: time
