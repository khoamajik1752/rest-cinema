from pydantic import BaseModel


class Ticket(BaseModel):
    InvoiceId: str
    MovieScheduleId: str
    Status:bool
    Seat:str