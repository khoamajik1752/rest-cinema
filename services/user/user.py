
from models import UserModel
from schemas import user_delete_request,user_delete_response,user_create_request,user_create_response,user_get_information_request,user_get_information_response,user_get_with_password_response,user_update_information_request,user_update_information_response,user_update_password_request,user_update_password_response,user_full_schema,user_without_password_schema
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument

class UserServices:
    @classmethod
    def remove_password(cls, data) -> user_without_password_schema:
        pass
        
        
    
    @classmethod
    def get_all_user(cls) -> list[user_get_information_response]:

        _user=UserModel.find()
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=user_get_information_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        
        return _res
    @classmethod
    def get_user(cls,form_data:user_get_information_request) -> user_get_information_response:
        id=form_data.id

        _user=UserModel.find_one({"_id":ObjectId(id)})
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=user_get_information_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        
        return _res
    
    @classmethod
    def get_user_with_password(cls,form_data:user_get_information_request) -> user_get_with_password_response:
        id=form_data.id

        _user=UserModel.find_one({"_id":ObjectId(id)})
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=user_get_with_password_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Password":_user.Password,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        
        return _res
     
    @classmethod
    def create_user(cls,form_data:user_create_request) -> user_create_response:
        username=form_data.Username
        password=form_data.Password
        fullname=form_data.Fullname
        email=form_data.Email
        tel=form_data.Tel

        _user=UserModel.insert_one({
            "Username":username,
            "Password":password,
            "Fullname":fullname,
            "Email":email,
            "Tel":tel,
            "Created_time":datetime.now,
            "Updated_time":datetime.now,
            "Last_login":None
            })
        
        
        if _user is None:
            raise Exception('Khong tao duoc user')
            
        _res=user_create_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        return _res
    
    @classmethod
    def update_user_information(cls,form_data:user_update_information_request) -> user_update_information_response:
        id=form_data.id
        fullname=form_data.Fullname
        email=form_data.Email
        tel=form_data.Tel
        _user=UserModel.find_one_and_update({"_id":ObjectId(id)},{
            "$set":{
            "Fullname":fullname,
            "Email":email,
            "Tel":tel,
            "Updated_time":datetime.now
            }
        },ReturnDocument.BEFORE)
        
        
        if _user is None:
            raise Exception('Khong thay user')
            
        _res=user_update_information_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        
        return _res
    
    @classmethod
    def update_user_password(cls,form_data:user_update_password_request) -> user_update_password_response:
        id=form_data.id
        oldPassword=form_data.oldPassword
        newPassword=form_data.newPassword
        
        if newPassword:
            pass#requirement for new password
        
        _user=UserModel.find_one_and_update({"_id":ObjectId(id),"Password":oldPassword},{
            "$set":{
            "Password":newPassword,
            "Updated_time":datetime.now
            }
        },ReturnDocument.BEFORE)
        
        
        if _user is None:
            raise Exception('password cu khong dung')
            
        _res=user_update_password_response({
            "id":_user._id.str,
            "Username":_user.Username,
            "Fullname":_user.Fullname,
            "Email":_user.Email,
            "Tel":_user.Tel,
            "Created_time":_user.Created_time,
            "Updated_time":_user.Updated_time,
            "Last_login":_user.Last_login
            })
        
        return _res
    
    @classmethod
    def delete_user(cls,form_data:user_delete_request) -> user_delete_response:
        id=form_data.id
        _user=UserModel.find_one_and_delete({"_id":ObjectId(id)},ReturnDocument.BEFORE)
        
        
        if _user is None:
            raise Exception('Khong thay user')
        
        return _user