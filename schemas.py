from pydantic import BaseModel
from typing import Union, Optional
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

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    isbn: str
    title: str
    genre: Genre

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    author: AuthorBase

    class Config:
        orm_mode = True


class TicketBase(BaseModel):
    id: int
    date_taken: datetime
    date_till: datetime

    class Config:
        orm_mode = True


class BookSchemaFull(BookBase):
    author: AuthorBase
    tickets: list[TicketBase]

    class Config:
        orm_mode = True


class AuthorCreate(BaseModel):
    name: str
    country: Union[int, str]


class AuthorSchema(AuthorBase):
    books: list[BookBase]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    id: int
    name: str
    phone: str
    address: Union[str, None] = None


class TicketSchema(TicketBase):
    user: UserBase
    book: BookSchema

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    tickets: list[TicketBase]

    class Config:
        orm_mode = True