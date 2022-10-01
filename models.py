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
    author_id = Column(Integer, ForeignKey("author.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))

    genre = relationship("Genre", back_populates="books")
    author = relationship("Author", back_populates="books")


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    books = relationship("Book", back_populates="genre")


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country", back_populates="authors")
    books = relationship("Book", back_populates="author")


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    authors = relationship("Author", back_populates="country")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(15), unique=True)
    address = Column(String(50), nullable=True)
    tickets = relationship("Ticket", back_populates="user")

    def __repr__(self):
        return f"User-{self.id} (Name={self.name}, Phone={self.phone}, Address={self.address})"

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("book.isbn"))
    user_id = Column(Integer, ForeignKey("user.id"))
    date_taken = Column(DateTime, default = datetime.now)
    date_till = Column(DateTime, default = calculate_book_borrow_period)
    
    book = relationship("Book")
    user = relationship("User")