from pydantic import Field, ConfigDict

from schemas.base import BasePublishedSchema, BaseCreatedAtSchema


class LocationCreateUpdateSchema(BasePublishedSchema):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(max_length=256, description="Name of the location")


class LocationSchema(BasePublishedSchema, BaseCreatedAtSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='ID')
    name: str = Field(max_length=256, description="Name of the location")
