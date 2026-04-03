from pydantic import Field, ConfigDict, BaseModel

from schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class CategoryCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    description: str = Field(description="Description")
    slug: str = Field(pattern=r'^[a-zA-Z0-9_-]+$', description="Identifier")


class CategoryUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(max_length=256, description="Title")
    description: str = Field(description="Description")


class CategorySchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    title: str = Field(max_length=256, description="Title")
    description: str = Field(description="Description")
    slug: str = Field(pattern=r'^[a-zA-Z0-9_-]+$', description="Identifier")
