from datetime import datetime

from pydantic import Field
from pydantic_extra_types.mime_types import Image

from src.schemas.users import UserSchema
from src.schemas.locations import LocationSchema
from src.schemas.categories import CategorySchema
from src.schemas.base import BaseCreatedAtSchema, BasePublishedSchema


class PostCreateSchema(BasePublishedSchema):
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    author: UserSchema = Field(description="Author")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location: LocationSchema = Field(description="Location")
    category: CategorySchema = Field(description="Category")
    image: Image


class PostUpdateSchema(BasePublishedSchema):
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    location: LocationSchema = Field(description="Location")
    category: CategorySchema = Field(description="Category")


class PostResponseSchema(BaseCreatedAtSchema, BasePublishedSchema):
    id: int = Field(description="ID")
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    author: UserSchema = Field(description="Author")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location: LocationSchema = Field(description="Location")
    category: CategorySchema = Field(description="Category")
    image: Image
