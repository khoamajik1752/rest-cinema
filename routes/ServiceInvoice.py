from fastapi import APIRouter
from models.ServiceInvoice import ServiceInvoice
from config.db import conn
from helpers import serializeDict, serializeList
from bson import ObjectId
serviceInvoice = APIRouter(
    prefix="/serviceInvoice",
    tags=['serviceInvoice']
)

@serviceInvoice.get('/')
async def find_all_ServiceInvoices():
    return serializeList(conn.local.ServiceInvoice.find())

@serviceInvoice.get('/{id}')
async def find_one_ServiceInvoice(id):
    return serializeDict(conn.local.ServiceInvoice.find_one({"_id":ObjectId(id)}))

@serviceInvoice.post('/')
async def create_ServiceInvoice(ServiceInvoice: ServiceInvoice):
    if (conn.local.Invoice.find_one({"_id":ObjectId(ServiceInvoice.InvoiceId)}) and conn.local.Service.find_one({"_id":ObjectId(ServiceInvoice.ServiceId)}) ):
        conn.local.ServiceInvoice.insert_one(dict(ServiceInvoice))
    return serializeDict(conn.local.ServiceInvoice.find())

@serviceInvoice.put('/{id}')
async def update_ServiceInvoice(id,ServiceInvoice: ServiceInvoice):
    if (conn.local.Invoice.find_one({"_id":ObjectId(ServiceInvoice.InvoiceId)}) and conn.local.Service.find_one({"_id":ObjectId(ServiceInvoice.ServiceId)}) ):
        conn.local.ServiceInvoice.find_one_and_update({"_id":ObjectId(id)},{
           "$set":dict(ServiceInvoice)
        })
    return serializeDict(conn.local.ServiceInvoice.find_one({"_id":ObjectId(id)}))

@serviceInvoice.delete('/{id}')
async def delete_ServiceInvoice(id):
    return serializeDict(conn.local.ServiceInvoice.find_one_and_delete({"_id":ObjectId(id)}))