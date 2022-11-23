from pydantic import BaseModel
from datetime import datetime



class TicketBase(BaseModel):
    id: int
    date_taken: datetime
    date_till: datetime
    
    class Config:
        orm_mode = True


class TicketUser(TicketBase):
    user: "UserBase"


class TicketBook(TicketBase):
    book: "BookAuthorGenre"


class Ticket(TicketBase):
    user: "UserBase"
    book: "BookAuthorGenre"


from .book import BookAuthorGenre
from .user import UserBase
Ticket.update_forward_refs()
TicketUser.update_forward_refs()
TicketBook.update_forward_refs()