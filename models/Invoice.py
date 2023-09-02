from pydantic import BaseModel
from datetime import datetime

class ServiceAmount():
    ServiceId:str
    Amount:str

class Invoice(BaseModel):
    CustomerId: str
    StaffId: str
    Date: datetime
    TotalPrice: float
    Status: str
    Name: str
    Email: str
    Tel: str
    Service: list[str]
    

    