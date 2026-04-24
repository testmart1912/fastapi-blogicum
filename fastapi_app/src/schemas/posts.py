from datetime import datetime

from pydantic import Field, ConfigDict

from src.schemas.users import UserSchema
from src.schemas.locations import LocationSchema
from src.schemas.categories import CategorySchema
from src.schemas.base import BaseCreatedAtSchema, BasePublishedSchema


class PostCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=256, description="Title")
    text: str = Field(min_length=1, description="Text")
    pub_date: datetime = Field(default_factory=datetime.today, description="Date of publication")
    location_id: int = Field(description="Location ID")
    category_id: int = Field(description="Category ID")
    image: str = Field(max_length=500, description="Image")


class PostUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=256, description="Title")
    text: str = Field(min_length=1, description="Text")
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
