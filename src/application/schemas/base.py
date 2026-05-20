from datetime import datetime
from typing import Annotated
import re

from pydantic import BaseModel, Field, AfterValidator, EmailStr


class BasePublishedSchema(BaseModel):
    is_published: bool = Field(True, description="Is published")

class BaseCreatedAtSchema(BaseModel):
    created_at: datetime = Field(description="Date of creation")


def validate_slug(value: str) -> str:
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise ValueError('Slug can only contain Latin letters, numbers, hyphens and underscores.')
    return value


SlugStr = Annotated[
    str,
    AfterValidator(validate_slug),
    Field(
        min_length=1,
        max_length=64,
        description='Page ID for URL: Latin characters, numbers, hyphens, and underscores.'
    ),
]


def validate_username(value: str) -> str:
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValueError('Username can only contain Latin letters, numbers and underscores.')
    return value


UsernameStr = Annotated[
    str,
    AfterValidator(validate_username),
    Field(
        min_length=3,
        max_length=150,
        description='Username: Latin letters, numbers and underscores.',
    ),
]


ValidatedEmail = Annotated[
    EmailStr|None,
    Field(description='Email'),
]
