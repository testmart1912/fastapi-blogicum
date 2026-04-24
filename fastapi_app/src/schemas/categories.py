from pydantic import Field, ConfigDict, BaseModel

from src.schemas.base import BasePublishedSchema, BaseCreatedAtSchema, SlugStr


class CategoryCreateSchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=256, description="Title")
    description: str = Field(min_length=1, max_length=2000, description="Description")
    slug: SlugStr


class CategoryUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(min_length=1, max_length=256, description="Title")
    description: str = Field(min_length=1, max_length=2000, description="Description")


class CategorySchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    title: str = Field(max_length=256, description="Title")
    description: str = Field(description="Description")
    slug: SlugStr
