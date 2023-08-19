from .schedule_schema import schedule_full_schema
from pydantic import BaseModel

class schedule_get_request(BaseModel):
    ScheduleID: str


class schedule_get_response(schedule_full_schema):
    pass
    