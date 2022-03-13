from typing import Optional, List

from pydantic import BaseModel, EmailStr


class ImageBase(BaseModel):
    url: Optional[str]