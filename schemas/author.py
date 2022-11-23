from pydantic import BaseModel


class AuthorBase(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class AuthorCountry(AuthorBase):
    country: "CountryBase"


class AuthorBooks(AuthorBase):
    books: "list[BookGenreTicket]"


class Author(AuthorBase):
    country: "CountryBase"
    books: "list[BookGenreTicket]"


from .country import CountryBase
from .book import BookGenreTicket
Author.update_forward_refs()
AuthorBooks.update_forward_refs()
AuthorCountry.update_forward_refs()