from pydantic import BaseModel


class AccessLvl(BaseModel):
    id: int


class AccessLvlCreate(BaseModel):
    id: int
    name: str
    code: int
