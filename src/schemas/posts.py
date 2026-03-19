from datetime import datetime

from pydantic import Field, ConfigDict

from src.schemas.users import UserSchema
from src.schemas.locations import LocationSchema
from src.schemas.categories import CategorySchema
from src.schemas.base import BaseCreatedAtSchema, BasePublishedSchema


class PostCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    author: int = Field(description="Author ID")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location: int = Field(description="Location ID")
    category: int = Field(description="Category ID")
    image: str = Field(description="Image")


class PostUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    location: int = Field(description="Location ID")
    category: int = Field(description="Category ID")


class PostResponseSchema(BaseCreatedAtSchema, BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description="ID")
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    author: UserSchema = Field(description="Author")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location: LocationSchema = Field(description="Location")
    category: CategorySchema = Field(description="Category")
    image: str = Field(description="Image")
