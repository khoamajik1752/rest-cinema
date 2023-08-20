from fastapi import APIRouter,Depends,HTTPException
from schemas.user import *
from db import conn
from models.User import User
from services.user.user import UserServices
user = APIRouter(
    prefix="/user",
    tags=['user']
    )

@user.get('/')
async def find_all_Users()->list[user_get_information_response]:
    a=UserServices.get_all_user()
    if a == []:
        raise HTTPException(status_code=404, detail="Item not found")
    return a

@user.get('/{id}')
async def find_one_User(id)->user_get_information_response:
    return UserServices.get_user(id)

@user.get('/psw/{id}')
async def find_one_User_with_password(id)->user_get_with_password_response:
    return UserServices.get_user_with_password(id)

@user.post('/')
async def create_User(User: user_create_request)->user_create_response:
    return UserServices.create_user(User)

@user.put('/{User.id}')
async def update_User(User: user_update_information_request)->user_update_information_response:
    return UserServices.update_user_information(User)

@user.put('/psw/{User.id}')
async def update_User_password(User: user_update_password_request)->user_update_password_response:
    return UserServices.update_user_password(User)

@user.delete('/{User.id}')
async def delete_User(User: user_delete_request)->user_delete_response:
    return UserServices.delete_user(User)