from pydantic import BaseModel 

class schedule_full_schema(BaseModel):
    SeatID:str
    Status:str
    