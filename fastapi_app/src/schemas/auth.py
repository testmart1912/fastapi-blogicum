from pydantic import Field, BaseModel

from src.resources.field_description import ACCESS_TOKEN
from src.resources.field_description import TOKEN_TYPE


class Token(BaseModel):
    access_token: str = Field(description=ACCESS_TOKEN)
    token_type: str = Field(description=TOKEN_TYPE)
