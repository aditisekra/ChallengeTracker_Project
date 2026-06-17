from pydantic import BaseModel, Field
from pydantic import EmailStr


class UserCreate(BaseModel):
    username: str=Field(min_length=3,max_length=20)
    email: EmailStr
    password: str=Field(min_length=8,max_length=20)


class UserLogin(BaseModel):
    email: EmailStr
    password: str=Field(min_length=8,max_length=20)


class UserUpdate(BaseModel):
    username: str | None =Field(default=None,min_length=3,max_length=20) 
    email: EmailStr | None = None


class UserResponse(BaseModel):
    id: int
    username: str=Field(min_length=3,max_length=20)
    email: EmailStr
    class Config:
        from_attributes = True