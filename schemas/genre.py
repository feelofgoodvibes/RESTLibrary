from pydantic import BaseModel


class GenreBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Genre(GenreBase):
    books: "list[BookAuthorTicket]"


from .book import BookAuthorTicket
Genre.update_forward_refs()