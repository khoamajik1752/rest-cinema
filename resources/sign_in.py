from fastapi import APIRouter,Depends
from helpers import security
from services import AuthService
from schemas import UserLogin
from typing import Annotated
from schemas import UserLogin
router=APIRouter(
    prefix="/auth",
    tags=["auth"],

    responses={404: {"description": "Not found"}},
)

@router.post("/sign_in")
async def sign_in(user_login:UserLogin):
    token= AuthService.sign_in(form_data=user_login.__dict__)    
    return token

@router.post("/test_auth")
async def test_auth( current_user: Annotated[UserLogin, Depends(security.get_current_active_user)]):

    return {}