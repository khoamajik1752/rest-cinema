
from models import UserModel
from schemas import user_delete_request,user_delete_response,user_create_request,user_create_response,user_get_information_request,user_get_information_response,user_get_with_password_response,user_update_information_request,user_update_information_response,user_update_password_request,user_update_password_response,user_full_schema,user_without_password_schema
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument

class UserServices:
    
    @classmethod
    def __remove_password(cls, data) -> user_without_password_schema:
        return {
            "id":str(data['_id']),
            "Username":data['Username'],
            "Fullname":data['Fullname'],
            "Email":data['Email'],
            "Tel":data['Tel'],
            "Created_time":data['Created_time'],
            "Updated_time":data['Updated_time'],
            "Last_login":data['Last_login']
        }
        
    @classmethod
    def __add_id(cls,data) -> user_full_schema:
        return{
            "id":str(data['_id']),
            "Username":data['Username'],
            "Password":data['Password'],
            "Fullname":data['Fullname'],
            "Email":data['Email'],
            "Tel":data['Tel'],
            "Created_time":data['Created_time'],
            "Updated_time":data['Updated_time'],
            "Last_login":data['Last_login']
        }    
        
    
    @classmethod
    def get_all_user(cls) -> list[user_get_information_response]:

        _users=UserModel.find()
        
        if _users is None:
            raise Exception('Khong thay user')
        _reslist= [cls.__remove_password(data) for data in _users]
        
        return _reslist
    
    @classmethod
    def get_user(cls,form_data:str) -> user_get_information_response:
        id=form_data

        _user=UserModel.find_one({"_id":ObjectId(id)})
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=cls.__remove_password(_user)
        
        return _res
    
    @classmethod
    def get_user_with_password(cls,form_data:user_get_information_request) -> user_get_with_password_response:
        id=form_data.id

        _user=UserModel.find_one({"_id":ObjectId(id)})
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=cls.__add_id(_user)
        
        return _res
     
    @classmethod
    def create_user(cls,form_data:user_create_request) -> user_create_response:
        username=form_data.Username
        password=form_data.Password
        fullname=form_data.Fullname
        email=form_data.Email
        tel=form_data.Tel

        userid=UserModel.insert_one({
            "Username":username,
            "Password":password,
            "Fullname":fullname,
            "Email":email,
            "Tel":tel,
            "Created_time":datetime.now(),
            "Updated_time":datetime.now(),
            "Last_login":datetime.now()
            })
        
        
        if userid is None:
            raise Exception('Khong tao duoc user')
        
        _res=cls.__remove_password(UserModel.find_one({"_id":ObjectId(userid.inserted_id)}))
        
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
            "Updated_time":datetime.now()
            }
        })
        
        
        if _user is None:
            raise Exception('Khong thay user')
          
        _res=cls.__remove_password(_user)  
        
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
            "Updated_time":datetime.now()
            }
        })
        
        
        if _user is None:
            raise Exception('password cu khong dung')
         
           
        _res=cls.__remove_password(_user)
        
        return _res
    
    @classmethod
    def delete_user(cls,form_data:user_delete_request) -> user_delete_response:
        id=form_data.id
        _user=UserModel.find_one_and_delete({"_id":ObjectId(id)})
        
        
        if _user is None:
            raise Exception('Khong thay user')
        
        _res=cls.__remove_password(_user)
        
        return _res