from pydantic import BaseModel


    
class ServiceInvoice(BaseModel):
    InvoiceId: str
    ServiceId: str