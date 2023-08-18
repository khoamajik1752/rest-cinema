from fastapi import APIRouter
from schemas import user_create_request,user_delete_request,user_update_information_request,user_get_information_request,user_update_password_request
from db import conn
from helpers import serializeDict, serializeList
from services.user.user import UserServices
user = APIRouter(
    prefix="/user",
    tags=['user']
    )

@user.get('/')
async def find_all_Users():
    return serializeList(conn.local.User.find())

@user.get('/{id}')
async def find_one_User(id):
    return serializeDict(conn.local.User.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_User(User: User):
    conn.local.User.insert_one(dict(User))
    return serializeDict(conn.local.User.find())

@user.put('/{id}')
async def update_User(id,User: User):
    conn.local.User.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(User)
    })
    return serializeDict(conn.local.User.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_User(id):
    return serializeDict(conn.local.User.find_one_and_delete({"_id":ObjectId(id)}))