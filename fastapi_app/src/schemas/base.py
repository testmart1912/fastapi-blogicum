from datetime import datetime

from pydantic import BaseModel, Field


class BasePublishedSchema(BaseModel):
    is_published: bool = Field(True, description="Is published")

class BaseCreatedAtSchema(BaseModel):
    created_at: datetime = Field(description="Date of creation")
