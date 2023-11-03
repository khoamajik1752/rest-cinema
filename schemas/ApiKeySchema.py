from datetime import datetime
from pydantic import BaseModel


class ApiKeyModel(BaseModel):
    api_key:str
    expired_date:datetime
    registered_date:datetime

class GetApiKeyRespModel(BaseModel):
    api_keys:list[ApiKeyModel]


class RegisterApiKeyReqModel(BaseModel):
    user_id:str

class RegisterApiKeyResModel(BaseModel):
    register_status:bool
    api_key:str=None
    # user_id:str
