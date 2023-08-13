from fastapi import APIRouter
from models.Ticket import Ticket
from config.db import conn
from schemas.Schemas import serializeDict, serializeList
from bson import ObjectId
ticket = APIRouter(
    prefix="/ticket",
    tags=['ticket']
)

@ticket.get('/')
async def find_all_Tickets():
    return serializeList(conn.local.Ticket.find())

@ticket.get('/{id}')
async def find_one_Ticket(id):
    return serializeDict(conn.local.Ticket.find_one({"_id":ObjectId(id)}))

@ticket.post('/')
async def create_Ticket(Ticket: Ticket):
    if (conn.local.Invoice.find_one({"_id":ObjectId(Ticket.InvoiceId)}) and conn.local.MovieSchedule.find_one({"_id":ObjectId(Ticket.MovieScheduleId)}) ):
        conn.local.Ticket.insert_one(dict(Ticket))
    return serializeDict(conn.local.Ticket.find())

@ticket.put('/{id}')
async def update_Ticket(id,Ticket: Ticket):
    if (conn.local.Invoice.find_one({"_id":ObjectId(Ticket.InvoiceId)}) and conn.local.MovieSchedule.find_one({"_id":ObjectId(Ticket.MovieScheduleId)}) ):
        conn.local.Ticket.find_one_and_update({"_id":ObjectId(id)},{
           "$set":dict(Ticket)
        })
    return serializeDict(conn.local.Ticket.find_one({"_id":ObjectId(id)}))

@ticket.delete('/{id}')
async def delete_Ticket(id):
    return serializeDict(conn.local.Ticket.find_one_and_delete({"_id":ObjectId(id)}))