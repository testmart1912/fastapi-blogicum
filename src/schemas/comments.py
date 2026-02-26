from pydantic import BaseModel, Field
from src.schemas.base import BaseCreatedAtSchema

from src.schemas.users import UserSchema

class CommentResponseSchema(BaseCreatedAtSchema):
    post: int = Field(description="Post ID")
    author: UserSchema = Field(description="Author")
    text: str = Field(description="Comment")

class CommentUpdateSchema(BaseModel):
    text: str = Field(description="Comment")

class CommentCreateSchema(BaseCreatedAtSchema):
    post: int = Field(description="Post ID")
    author: UserSchema = Field(description="Author")
    text: str = Field(description="Comment")
