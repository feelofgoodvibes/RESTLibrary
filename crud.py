from sqlalchemy.orm import Session
from models import Genre, User, Country, Author, Book, Ticket
from schemas import genre, user, country, author, book, ticket


def get_genres(db: Session, limit: int = None, offset: int = None):
    return db.query(Genre).limit(limit).offset(offset).all()


def get_countries(db: Session, limit: int = None, offset: int = None):
    return db.query(Country).limit(limit).offset(offset).all()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_authors(db: Session, limit: int = None, offset: int = None):
    return db.query(Author).limit(limit).offset(offset).all()


# def create_author(db: Session, author: schemas.AuthorCreate):
#     if isinstance(author.country, int):
#         country = db.query(Country).filter(Country.id == author.country).first()

#     elif isinstance(author.country, str):
#         country = db.query(Country).filter(Country.name == author.country).first()

#     if country is None:
#         return None

#     new_author = Author(name=author.name, country_id=country.id)
#     db.add(new_author)
#     db.commit()
#     db.refresh(new_author)

#     return new_author


def get_book(db: Session, book_isbn: int):
    return db.query(Book).filter(Book.isbn == book_isbn).first()


def get_books(db: Session, limit: int = None, offset: int = None):
    return db.query(Book).limit(limit).offset(offset).all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def get_tickets(db: Session, limit: int = None, offset: int = None):
    return db.query(Ticket).limit(limit).offset(offset).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, limit: int = None, offset: int = None):
    return db.query(User).limit(limit).offset(offset).all()
