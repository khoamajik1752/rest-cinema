from .schedule_schema import schedule_full_schema
from pydantic import BaseModel
class schedule_delete_request(BaseModel):
    ScheduleId:str

class schedule_delete_response(schedule_full_schema):
    pass
    