from sqlalchemy.orm import Session
from models import Genre, User, Country, Author, Book, Ticket


def get_genres(db: Session):
    return db.query(Genre).all()


def get_countries(db: Session):
    return db.query(Country).all()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_authors(db: Session):
    return db.query(Author).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(db: Session):
    return db.query(Book).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def get_tickets(db: Session):
    return db.query(Ticket).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session):
    return db.query(User).all()