from pydantic import BaseModel
from country import Country
from book import BookGenreTicket


class AuthorBase(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class AuthorCountry(AuthorBase):
    country: Country


class AuthorBooks(AuthorBase):
    books: list[BookGenreTicket]