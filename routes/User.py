from fastapi import APIRouter
from schemas import user_create_request,user_delete_request,user_update_information_request,user_get_information_request,user_update_password_request
from db import conn
from models.User import User
from helpers import serializeDict, serializeList
from services.user.user import UserServices
user = APIRouter(
    prefix="/user",
    tags=['user']
    )

@user.get('/')
async def find_all_Users():
    return serializeList(UserServices.get_all_user())

@user.get('/{id}')
async def find_one_User(id):
    return serializeDict(UserServices.get_user(id))

@user.get('/psw/{id}')
async def find_one_User_with_password(id):
    return serializeDict(UserServices.get_user_with_password(id))

@user.post('/')
async def create_User(User: user_create_request):
    return serializeDict(UserServices.create_user(User))

@user.put('/{User.id}')
async def update_User(User: user_update_information_request):
    return serializeDict(UserServices.update_user_information(User))

@user.put('/psw/{User.id}')
async def update_User(User: user_update_password_request):
    return serializeDict(UserServices.update_user_password(User))

@user.delete('/{User.id}')
async def delete_User(User: user_delete_request):
    return serializeDict(UserServices.delete_user(User))