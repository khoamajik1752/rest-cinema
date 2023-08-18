from .user_schema import user_without_password_schema
from pydantic import BaseModel
class user_delete_request(BaseModel):
    id:str

class user_delete_response(user_without_password_schema):
    pass
    