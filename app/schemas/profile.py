from typing import Optional, List

from pydantic import BaseModel, EmailStr

from app.schemas.image import ImageBase


class ProfileBase(BaseModel):
    full_name: Optional[str]
    avatar: Optional[ImageBase]