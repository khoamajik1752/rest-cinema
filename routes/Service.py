from fastapi import APIRouter
from models.Service import Service
from db import conn
from helpers import serializeDict, serializeList
from bson import ObjectId
service = APIRouter(
    prefix="/service",
    tags=['service']
    )

@service.get('/')
async def find_all_Services():
    return serializeList(conn.local.Service.find())

@service.get('/{id}')
async def find_one_Service(id):
    return serializeDict(conn.local.Service.find_one({"_id":ObjectId(id)}))

@service.post('/')
async def create_Service(Service: Service):
    conn.cinema.Service.insert_one(dict(Service))
    return serializeDict(conn.cinema.Service.find())

@service.put('/{id}')
async def update_Service(id,Service: Service):
    conn.cinema.Service.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Service)
    })
    return serializeDict(conn.cinema.Service.find_one({"_id":ObjectId(id)}))

@service.delete('/{id}')
async def delete_Service(id):
    return serializeDict(conn.local.Service.find_one_and_delete({"_id":ObjectId(id)}))