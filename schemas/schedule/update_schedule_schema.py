from .schedule_schema import schedule_full_schema
from pydantic import BaseModel

class schedule_update_request(BaseModel):
    ScheduleID: str
    SeatID: str
    Status: str


class schedule_update_response(schedule_full_schema):
    pass
    