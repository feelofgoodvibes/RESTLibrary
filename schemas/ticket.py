from pydantic import BaseModel
from book import BookAuthorGenre
from datetime import datetime

from user import UserBase


class TicketBase(BaseModel):
    id: int
    date_taken: datetime
    date_till: datetime
    
    class Config:
        orm_mode = True


class TicketUser(TicketBase):
    user: UserBase


class TicketBook(TicketBase):
    book: BookAuthorGenre