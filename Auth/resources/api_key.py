import datetime
from fastapi import APIRouter, Depends
from helpers import security
from schemas import ApiKeySchema
from model import ApiKeyModel
from bson import ObjectId
from pymongo import collection
from services import APIKeyService
import secrets

router=APIRouter(
    prefix="/api_key",
    tags=["API key"],
    dependencies=[Depends(security.security)],
)

@router.get("/get")
def get_api_key(_user_id:str):
   api_keys= APIKeyService.get_api_key(_user_id)
   return api_keys
@router.post("/register")
def register_api_key(data:ApiKeySchema.RegisterApiKeyReqModel):
    _key=   secrets.token_urlsafe(16)
    _api_key=ApiKeyModel.find({
        "api_key":_key
    })

    while _api_key ==None:
        _key=   secrets.token_urlsafe(16)
        _api_key=ApiKeyModel.find({
            "api_key":_key
        })

    
    _api_key=ApiKeyModel.insert_one({
        "user_id":ObjectId(data.user_id),
        "api_key":_key,
        "expired_date":datetime.datetime.now(),
        "registered_date":datetime.datetime.now()
    })

    return ApiKeySchema.RegisterApiKeyResModel(register_status=True,access_key=_key)


