from models import InvoiceModel,StaffModel,UserModel
from schemas import create_invoice_request,update_invoice
from bson import ObjectId
from fastapi import FastAPI, HTTPException
class InvoiceServices:
    @classmethod
    def create_invoice(form_data:create_invoice_request):
        staff_id=form_data.Staff_ID
        user_id=form_data.CusID
        _staff=StaffModel.find_one({"_id":ObjectId(staff_id)})
        if _staff is None:
            raise HTTPException(status_code=404, detail="Staff not found")
        _user=UserModel.find_one({"_id":ObjectId(user_id)})
        if _user is None:
            raise HTTPException(status_code=404, detail="User not found")            
        InvoiceModel.insert_one(form_data)
        return {
            "status":"OK"
        }
    @classmethod
    def update_invoice(form_data:update_invoice):

        id=form_data.id
        InvoiceModel.update({"_id":ObjectId(id)},)