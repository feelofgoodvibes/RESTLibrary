from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    name: str
    phone: str
    address: str

    class Config:
        orm_mode = True


class User(UserBase):
    tickets: "list[TicketBook]"


from .ticket import TicketBook
User.update_forward_refs()