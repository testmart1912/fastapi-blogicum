from pydantic import BaseModel, Field, ConfigDict

from src.schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class CommentResponseSchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    post_id: int = Field(description="Post ID")
    author_id: int = Field(description="Author ID")
    text: str = Field(description="Comment")


class CommentUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str = Field(description="Comment")


class CommentCreateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    post_id: int = Field(description="Post ID")
    author_id: int = Field(description="Author ID")
    text: str = Field(description="Comment")
