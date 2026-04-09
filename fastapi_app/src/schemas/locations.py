from pydantic import Field, ConfigDict

from src.schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class LocationCreateUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(min_length=1, max_length=256, description="Name of the location")


class LocationSchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    name: str = Field(min_length=1, max_length=256, description="Name of the location")
