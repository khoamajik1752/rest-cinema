
from dependencies import pwd_context
from model import UserModel
from datetime import datetime, timedelta
from config import Config
from jose import JWTError, jwt

class AuthService:
    @classmethod
    def sign_up(cls,form_data:dict):
    
        form_data["password"]=pwd_context.hash(form_data["password"])
        UserModel.insert_one({
            **form_data
        })
    
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)    
    
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
        username=form_data["username"]
        password=form_data["password"]

        user = UserModel.find_one({
            "username":username
            }
        )
        print(user)
        hashed_password=user["password"]
        print(hashed_password)
        if not user:
            return False
        
        if not cls.verify_password(password, hashed_password):
            return False
        
        token= cls.create_access_token(data={"name":"khoa"})
        return token