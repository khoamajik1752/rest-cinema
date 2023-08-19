from .schedule_schema import schedule_full_schema
from pydantic import BaseModel

class schedule_create_request(BaseModel):
    ScheduleID:str
    SeatID:str
    

class schedule_create_response(schedule_full_schema):
    pass
    