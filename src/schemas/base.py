from pydantic import BaseModel, Field
from datetime import datetime


class BasePublishedSchema(BaseModel):
    is_published: bool = Field(True, description="Is published")

class BaseCreatedAtSchema(BaseModel):
    created_at: datetime = Field(description="Date of creation")