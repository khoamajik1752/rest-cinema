from pydantic import BaseModel




class SignUpUser(BaseModel):
    username: str
    password: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None