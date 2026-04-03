from datetime import datetime

from pydantic import Field, ConfigDict

from schemas.users import UserSchema
from schemas.locations import LocationSchema
from schemas.categories import CategorySchema
from schemas.base import BaseCreatedAtSchema, BasePublishedSchema


class PostCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    author_id: int = Field(description="Author ID")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location_id: int = Field(description="Location ID")
    category_id: int = Field(description="Category ID")
    image: str = Field(description="Image")


class PostUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    text: str = Field(description="Text")
    location_id: int = Field(description="Location ID")
    category_id: int = Field(description="Category ID")


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
