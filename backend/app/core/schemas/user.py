from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    last_name: str = Field(..., alias="lastName")
    gender: str
    phone_number: str = Field(..., alias="phoneNumber")
    email: str
    address: str
    photo: str


class UserCreate(UserBase):
    pass
