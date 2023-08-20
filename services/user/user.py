
from models import UserModel
from schemas.user import * 
from bson import ObjectId
from helpers.CustomModel import CustomModel

class UserServices:
    
    model=CustomModel(UserModel)
    
    @classmethod
    def get_all_user(cls)->list[user_get_information_response]:
        
        pipeline=[ { '$match': {} },{'$set':{'_id':{'$toString': "$_id"}}} ]
        _res=cls.model.aggregate(pipeline)
        
        return _res
    
    @classmethod
    def get_user(cls,form_data:str) -> user_get_information_request:
        id=form_data
        
        pipeline=[ { '$match': {'_id':ObjectId(id)} },{'$set':{'_id':{'$toString': "$_id"}}} ]
        _res=cls.model.aggregate(pipeline).pop()
        
        
        return _res
    
    @classmethod
    def get_user_with_password(cls,form_data:user_get_information_request) -> user_get_with_password_response:
        id=form_data.id
        
        pipeline=[ { '$match': {'_id':ObjectId(id)} },{'$set':{'_id':{'$toString': "$_id"}}} ]
        _res=cls.model.aggregate(pipeline).pop()
        
        return _res
     
    @classmethod
    def create_user(cls,form_data:user_create_request) -> user_create_response:
        
        data=user_full_schema(**dict(form_data))
        _res=cls.model.insert_one(dict(data))
        
        return _res
    
    @classmethod
    def update_user_information(cls,form_data:user_update_information_request) -> user_update_information_response:
        data = user_update_information_schema_mapping(**dict(form_data))
        filter={"_id":ObjectId(form_data.id)}
        update={"$set":dict(data)}
        _res=cls.model.find_one_and_update(filter,update)
        
        return _res
    
    @classmethod
    def update_user_password(cls,form_data:user_update_password_request) -> user_update_password_response:
        data=user_update_password_schema_mapping(**dict(form_data))
        print(data)
        if data.Password:
            pass#requirement for new password
        
        filter={"_id":ObjectId(form_data.id),"Password":form_data.oldPassword}
        update={"$set":dict(data)}
        _res=cls.model.find_one_and_update(filter,update)
        
         
        
        return _res
    
    @classmethod
    def delete_user(cls,form_data:user_delete_request) -> user_delete_response:
        
        filter={"_id":ObjectId(form_data.id)}
        _res=cls.model.find_one_and_delete(filter)
        
        return _res