from pydantic import BaseModel


class CountryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Country(CountryBase):
    authors: "list[AuthorBase]"


from .author import AuthorBase
Country.update_forward_refs()
