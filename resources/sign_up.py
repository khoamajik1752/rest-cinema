from fastapi import APIRouter,Depends
from schemas import SignUpUser
from model import UserModel
from services import AuthService
router=APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)

@router.post("/sign_up")
async def sign_up(form_data:SignUpUser):

    AuthService.sign_up(form_data=form_data.__dict__)
    
    return True