from fastapi import Depends, Request, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Annotated
from config import Config
from model import UserModel
from schemas import UserLogin
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=Config.TOKEN_URL)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        # print(payload)
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user= UserModel.find_one({
        "username":username
    })

    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserLogin, Depends(get_current_user)]
):
    # print(current_user)
    is_disabled=current_user.get('disabled')
    if is_disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def security(
    request:Request,
    current_active_user:Annotated[UserLogin, Depends(get_current_active_user)]
):
    _Origin=request.headers["Origin"]
    _url=str(request.url)
    _permission=_url.replace(_Origin,"").split("/")[0]
    _roles=current_active_user.get("roles")

    authorize_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not authorize user",
        headers={"WWW-Authorize": "Bearer"},
    )

    if _roles is None or len(_roles)==0:
        raise authorize_exception
    if _permission not in _roles:
        raise authorize_exception 
    else:
        return current_active_user
    