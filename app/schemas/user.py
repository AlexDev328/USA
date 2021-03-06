from typing import Optional, List

from pydantic import BaseModel, EmailStr

# Shared properties
from app.schemas.profile import ProfileBase
from app.schemas.accesslvl import AccessLvl


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    access: Optional[AccessLvl] = None
    username: str


class UserProfile(UserBase):
    profile: Optional[ProfileBase]


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
