from fastapi import APIRouter
from models.Staff import Staff
from config.db import conn
from helpers import serializeDict, serializeList
from bson import ObjectId
staff = APIRouter(
    prefix="/staff",
    tags=['staff']
    )

@staff.get('/')
async def find_all_Staffs():
    return serializeList(conn.local.Staff.find())

@staff.get('/{id}')
async def find_one_Staff(id):
    return serializeDict(conn.local.Staff.find_one({"_id":ObjectId(id)}))

@staff.post('/')
async def create_Staff(Staff: Staff):
    conn.local.Staff.insert_one(dict(Staff))
    return serializeDict(conn.local.Staff.find())

@staff.put('/{id}')
async def update_Staff(id,Staff: Staff):
    conn.local.Staff.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Staff)
    })
    return serializeDict(conn.local.Staff.find_one({"_id":ObjectId(id)}))

@staff.delete('/{id}')
async def delete_Staff(id):
    return serializeDict(conn.local.Staff.find_one_and_delete({"_id":ObjectId(id)}))