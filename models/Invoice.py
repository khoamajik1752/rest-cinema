from pydantic import BaseModel
from datetime import datetime


class Invoice(BaseModel):
    CustomerId: str
    StaffId: str
    Date: datetime
    TotalPrice: float
    Status: str
    Name: str
    Email: str
    Tel: str
    