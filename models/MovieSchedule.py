from pydantic import BaseModel, validator
from datetime import datetime, date


    
class MovieSchedule(BaseModel):
    DateStartTime: datetime
    Room:int
    Price:float
    MovieId: str
    