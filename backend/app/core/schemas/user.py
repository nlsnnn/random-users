from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    name: str
    last_name: str = Field(..., serialization_alias="lastName")
    gender: str
    phone_number: str = Field(..., serialization_alias="phoneNumber")
    email: str
    address: str
    photo: str


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserCreateRequest(BaseModel):
    count: int
