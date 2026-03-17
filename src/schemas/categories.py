from pydantic import Field

from src.schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class CategorySchema(BasePublishedSchema, BaseCreatedAtSchema):
    title: str = Field(max_length=256, description="Title")
    description: str = Field(description="Description")
    slug: str = Field(pattern=r'^[a-zA-Z0-9_-]+$', description="Identifier")
