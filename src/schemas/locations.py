from pydantic import Field

from src.schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class LocationSchema(BasePublishedSchema, BaseCreatedAtSchema):
    name: str = Field(max_length=256, description="Name of the location")
