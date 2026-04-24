from pydantic import BaseModel, Field, ConfigDict

from src.schemas.base import BaseCreatedAtSchema, BasePublishedSchema


class CommentResponseSchema(BaseCreatedAtSchema, BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    post_id: int = Field(description="Post ID")
    author_id: int = Field(description="Author ID")
    text: str = Field(description="Comment")


class CommentUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str = Field(min_length=1, max_length=256, description="Comment")


class CommentCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    post_id: int = Field(description="Post ID")
    text: str = Field(min_length=1, max_length=256, description="Comment")
