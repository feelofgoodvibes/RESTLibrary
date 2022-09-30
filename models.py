from email.policy import default
from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_book_borrow_period():
    return datetime.now() + relativedelta(month=1)


class Book(Base):
    __tablename__ = "book"

    isbn = Column(String(20), primary_key=True)
    title = Column(String(100))
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    country = relationship("Country", back_populates="authors")


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(15), unique=True)
    address = Column(String(50))
    tickets = relationship("Ticket", back_populates="owner")


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book = relationship("Book", back_populates="tickets")
    date_taken = Column(DateTime, default = datetime.now)
    date_till = Column(DateTime, default = calculate_book_borrow_period)