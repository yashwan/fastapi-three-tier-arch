from pydantic import BaseModel, Field, EmailStr
from uuid import UUID


class User(BaseModel):
    username: str = Field(min_length=3)
    email: str = EmailStr()
    password: str = Field(min_length=6)

    class Config:
        orm_mode = True
