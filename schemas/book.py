from pydantic import BaseModel
from author import AuthorBase
from genre import GenreBase
from ticket import TicketBase


class BookBase(BaseModel):
    isbn: str
    title: str

    class Config:
        orm_mode = True


class BookAuthorTicket(BookBase):
    author: AuthorBase
    tickets: list[TicketBase]


class BookGenreTicket(BookBase):
    genre: GenreBase
    tickets: list[TicketBase]


class BookAuthorGenre(BookBase):
    author: AuthorBase
    genre: GenreBase