from pydantic import BaseModel


class BookBase(BaseModel):
    isbn: str
    title: str

    class Config:
        orm_mode = True


class BookAuthorTicket(BookBase):
    author: "AuthorBase"
    tickets: "list[TicketUser]"


class BookGenreTicket(BookBase):
    genre: "GenreBase"
    tickets: "list[TicketUser]"


class BookAuthorGenre(BookBase):
    author: "AuthorBase"
    genre: "GenreBase"


class Book(BookBase):
    author: "AuthorBase"
    genre: "GenreBase"
    tickets: "list[TicketUser]"


from .author import AuthorBase
from .genre import GenreBase
from .ticket import TicketUser
Book.update_forward_refs()
BookGenreTicket.update_forward_refs()
BookAuthorGenre.update_forward_refs()
BookAuthorTicket.update_forward_refs()