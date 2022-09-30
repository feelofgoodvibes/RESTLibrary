from pydantic import BaseModel
from datetime import datetime


class Country(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Genre(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    id: int
    name: str
    country: Country


class BookBase(BaseModel):
    isbn: str
    title: str
    genre: Genre


class BookSchema(BookBase):
    author: AuthorBase

    class Config:
        orm_mode = True


class AuthorSchema(AuthorBase):
    books: list[BookBase]

    class Config:
        orm_mode = True


class TicketBase(BaseModel):
    id: int
    book: BookSchema
    date_taken: datetime
    date_till: datetime


class UserBase(BaseModel):
    id: int
    name: str
    phone: str
    address: str


class TicketSchema(TicketBase):
    user: UserBase

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    tickets: list[TicketBase]

    class Config:
        orm_mode = True