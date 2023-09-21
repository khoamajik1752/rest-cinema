

from model import UserModel
from datetime import datetime, timedelta
from config import Config
from jose import JWTError, jwt



class AuthService:
    @classmethod
    def sign_up(cls,form_data:dict):
        form_data["username"]=form_data["username"].lower()
        form_data["password"]=Config.pwd_context.hash(form_data["password"])
        form_data["roles"]=['user']
        UserModel.insert_one({
            **form_data
        })
        
    
    def verify_password(plain_password, hashed_password):
        return Config.pwd_context.verify(plain_password, hashed_password)    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
        return encoded_jwt
    
    @classmethod
    def sign_in(cls,form_data:dict):
        username=form_data["username"].lower()
        password=form_data["password"]

        user = UserModel.find_one({
            "username":username
            }
        )
        hashed_password=user["password"]
        if not user:
            return False
        
        if not cls.verify_password(password, hashed_password):
            return False
        user.pop('_id',None)
        token= cls.create_access_token(data=user)
  
        return token