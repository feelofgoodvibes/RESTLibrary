from pydantic import BaseModel
from ticket import TicketBook


class UserBase(BaseModel):
    id: int
    name: str
    phone: str
    address: str

    class Config:
        orm_mode = True


class UserFull(UserBase):
    tickets: list[TicketBook]