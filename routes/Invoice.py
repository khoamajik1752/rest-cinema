from fastapi import APIRouter
from models.Invoice import Invoice
from config.db import conn
from schemas.Schemas import serializeDict, serializeList
from bson import ObjectId
invoice = APIRouter(
    prefix="/invoice",
    tags=['invoice']
)

@invoice.get('/')
async def find_all_Invoices():
    return serializeList(conn.local.Invoice.find())

@invoice.get('/{id}')
async def find_one_Invoice(id):
    return serializeDict(conn.local.Invoice.find_one({"_id":ObjectId(id)}))

@invoice.post('/')
async def create_Invoice(Invoice: Invoice):
    if conn.local.Staff.find_one({"_id":ObjectId(Invoice.StaffId)}):
        temp=serializeDict(conn.local.User.find_one({"_id":ObjectId(Invoice.CustomerId)}))
        if temp:
            Invoice.Name=temp['Username']
            Invoice.Email=temp['Email']
            Invoice.Tel=temp['Tel']
        conn.local.Invoice.insert_one(dict(Invoice))
    return serializeDict(conn.local.Invoice.find())

@invoice.put('/{id}')
async def update_Invoice(id,Invoice: Invoice):
    if conn.local.Staff.find_one({"_id":ObjectId(Invoice.StaffId)}):
        temp=serializeDict(conn.local.User.find_one({"_id":ObjectId(Invoice.CustomerId)}))
        if temp:
            Invoice.Name=temp['Username']
            Invoice.Email=temp['Email']
            Invoice.Tel=temp['Tel']
        conn.local.Invoice.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Invoice)
        })
    return serializeDict(conn.local.Invoice.find_one({"_id":ObjectId(id)}))

@invoice.delete('/{id}')
async def delete_Invoice(id):
    return serializeDict(conn.local.Invoice.find_one_and_delete({"_id":ObjectId(id)}))