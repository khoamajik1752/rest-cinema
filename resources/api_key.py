import datetime
from fastapi import APIRouter, Depends
from helpers import security
from schemas import ApiKeySchema
from model import ApiKeyModel
from bson import ObjectId
from pymongo import collection

import secrets

router=APIRouter(
    prefix="/api_key",
    tags=["API key"],
    dependencies=[Depends(security.security)],
)

@router.get("/get")
def get_api_key(_user_id:str):
    _api_keys= ApiKeyModel.find({
        "user_id":ObjectId(_user_id)
    })
    api_keys=[]
    for _api_key in _api_keys:
        key=_api_key["api_key"]
        expired_date=_api_key["expired_date"]
        registered_date=_api_key["registered_date"]
        api_keys.append(ApiKeySchema.ApiKeyModel(api_key=key,expired_date=expired_date,registered_date=registered_date))

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

    return ApiKeySchema.RegisterApiKeyResModel(register_status=True,api_key=_key)


