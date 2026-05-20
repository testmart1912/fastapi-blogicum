from datetime import datetime
from typing import Optional

from pydantic import BaseModel, SecretStr, ConfigDict, Field

from application.schemas.base import UsernameStr, ValidatedEmail


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: UsernameStr
    first_name: str = Field(min_length=1, max_length=150, description='Name')
    last_name: str = Field(min_length=1, max_length=150, description='Surname')
    email: ValidatedEmail | None
    password: SecretStr
    is_staff: bool
    is_active: bool
    is_superuser: bool
    last_login: Optional[datetime]
    date_joined: datetime


class UserCreateUpdateSchema(BaseModel):
    username: UsernameStr = Field(description='Username')
    password: str = Field(min_length=8, max_length=128, description='Password')
    email: ValidatedEmail | None = Field(None, description='Email')
    first_name: str = Field('', max_length=150, description='Name')
    last_name: str = Field('', max_length=150, description='Surname')


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: UsernameStr
    first_name: str
    last_name: str
    email: ValidatedEmail | None
    is_active: bool
    date_joined: datetime
