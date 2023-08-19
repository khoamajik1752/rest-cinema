from pydantic import BaseModel



class create_invoice_request(BaseModel):
    CusID: str
    Staff_ID: str


class create_invoice_response(BaseModel):
    id:str