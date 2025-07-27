from pydantic import BaseModel, EmailStr, constr

class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserRegisterResponse(BaseModel):
    message: str
