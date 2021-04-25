from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

from app.models.core import IDModelMixin, CoreModel

# Shared properties
class UserBase(CoreModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# Additional properties stored in DB
class UserInDB(IDModelMixin, UserBase):
    hashed_password: str
    created_at: datetime


# Additional properties to return via API
class UserPublic(IDModelMixin, UserBase):
    pass



