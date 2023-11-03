from fastapi import APIRouter,Depends
from helpers import security
from services import AuthService
from schemas import UserLogin
from typing import Annotated
from schemas import UserLogin, loginResponse
router=APIRouter(
    prefix="/auth",
    tags=["auth"],

    responses={404: {"description": "Not found"}},
)

@router.post("/sign_in",response_model=loginResponse)
async def sign_in(user_login:UserLogin):
    token= AuthService.sign_in(form_data=user_login.__dict__)    
    return loginResponse(access_token=token)

# @router.post("/test_auth",response_model=UserLogin)
# async def test_auth( current_user: Annotated[UserLogin, Depends(security.security)]):

#     return current_user