from pydantic import BaseModel
from datetime import datetime

class ServiceAmount():
    ServiceId:str
    Amount:str
    
    def __init__(self,id,amount):
        self.ServiceId=id
        self.Amount=amount

class Invoice(BaseModel):
    CustomerId: str
    StaffId: str
    Date: datetime
    TotalPrice: float
    Status: str
    Name: str
    Email: str
    Tel: str
    Service: list[ServiceAmount]
    

    