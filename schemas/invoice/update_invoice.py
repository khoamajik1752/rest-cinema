from pydantic import BaseModel
from typing import Optional


class update_invoice_request(BaseModel):
    id:str
    food_service: Optional[list[str]]
    status:Optional[str]


