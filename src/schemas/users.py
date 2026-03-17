from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, SecretStr


class UserSchema(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    passwd: SecretStr
    is_staff: bool
    is_active: bool
    is_superuser: bool
    last_login: datetime
    date_joined: date
