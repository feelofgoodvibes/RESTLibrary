from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models
from schemas import country, genre, author, book, ticket, user
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Country ---------------------------------------------


@app.get("/countries/", response_model=list[country.Country])
def get_countries(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    # countries = crud.get_countries(db, limit=limit, offset=offset)
    countries = crud.get_collection(db, models.Country, limit=limit, offset=offset)
    return countries


@app.post("/countries/", response_model=country.CountryBase)
def create_country(country: country.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(country, db)


# Genre -----------------------------------------------


@app.get("/genres/", response_model=list[genre.Genre])
def get_genres(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    genres = crud.get_collection(db, models.Genre, limit=limit, offset=offset)
    return genres

# Author ----------------------------------------------


@app.get("/authors/", response_model=list[author.Author])
def get_genres(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    authors = crud.get_collection(db, models.Author, limit=limit, offset=offset)
    return authors
    

@app.get("/authors/{author_id}", response_model=author.Author)
def get_country(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_collection_item(db, models.Author, models.Author.id, author_id)

    if not author:
        raise HTTPException(status_code=404, detail=f"Author with id {author_id} does not exists")

    return author


# @app.post("/authors/", response_model=schemas.AuthorSchema)
# def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
#     db_author = crud.create_author(db, author)

#     if db_author is None:
#         raise HTTPException(status_code=404, detail="Wrong country")

#     return db_author

# Book ---------------------------------------------


@app.get("/books/", response_model=list[book.Book])
def get_books(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    books = crud.get_collection(db, models.Book, limit=limit, offset=offset)
    return books
    

@app.get("/books/{book_isbn}", response_model=book.Book)
def get_book(book_isbn: int, db: Session = Depends(get_db)):
    book = crud.get_collection_item(db, models.Book, models.Book.isbn, book_isbn)

    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_isbn} does not exists")

    return book

# Ticket -------------------------------------------


@app.get("/tickets/", response_model=list[ticket.Ticket])
def get_tickets(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    tickets = crud.get_collection(db, models.Ticket, limit=limit, offset=offset)
    return tickets
    

@app.get("/tickets/{ticket_id}", response_model=ticket.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_collection_item(db, models.Ticket, models.Ticket.id, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail=f"Ticket with id {ticket_id} does not exists")

    return ticket

# User ---------------------------------------------


@app.get("/users/", response_model=list[user.User])
def get_users(limit: int = None, offset: int = None, db: Session = Depends(get_db)):
    users = crud.get_collection(db, models.User, limit=limit, offset=offset)
    return users
    

@app.get("/users/{user_id}", response_model=user.User)
def get_ticket(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_collection_item(db, models.User, models.User.id, user_id)

    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exists")

    return user
