from pydantic import BaseModel, Field


class ListParams(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(50, ge=1, le=200, alias="pageSize")


class ScoreByAddressParams(BaseModel):
    address: str
    city: str | None = None
    state: str | None = None
    postal_code: str | None = Field(None, alias="postalCode")