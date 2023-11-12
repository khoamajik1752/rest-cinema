


from datetime import datetime,timedelta
import secrets
from bson import ObjectId
from model import ApiKeyModel
from schemas import ApiKeySchema


class APIKeyService:
    @classmethod
    def get_api_key(cls,_user_id:str):
        _api_keys:list[dict]= ApiKeyModel.find({
            "user_id":ObjectId(_user_id)
        })
        api_keys=[]
        for _api_key in _api_keys:
            key=_api_key.get("access_key")
            expired_date=_api_key["expired_date"]
            registered_date=_api_key["registered_date"]
            api_keys.append(ApiKeySchema.ApiKeyModel(api_key=key,expired_date=expired_date,registered_date=registered_date))

        return api_keys
    @classmethod
    def register_api_key(cls,data:ApiKeySchema.RegisterApiKeyReqModel):
        _access_key=   secrets.token_urlsafe(16)
        _api_key=ApiKeyModel.find({
            "access_key":_access_key
        })

        while _api_key ==None:
            _access_key=   secrets.token_urlsafe(16)
            _api_key=ApiKeyModel.find({
                "access_key":_access_key
            })

        
        _api_key=ApiKeyModel.insert_one({
            "user_id":ObjectId(data.user_id),
            "access_key":_access_key,
            "expired_date":datetime.now() +timedelta(days=24),
            "registered_date":datetime.now()
        })

        return ApiKeySchema.RegisterApiKeyResModel(register_status=True,api_key=_access_key)