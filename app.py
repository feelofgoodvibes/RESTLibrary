from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
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


@app.get("/countries/", response_model=list[schemas.Country])
def get_countries(db: Session = Depends(get_db)):
    countries = crud.get_countries(db)
    return countries

# Genre -----------------------------------------------


@app.get("/genres/", response_model=list[schemas.Genre])
def get_genres(db: Session = Depends(get_db)):
    genres = crud.get_genres(db)
    return genres

# Author ----------------------------------------------


@app.get("/authors/", response_model=list[schemas.AuthorSchema])
def get_genres(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors
    

@app.get("/authors/{author_id}", response_model=schemas.AuthorSchema)
def get_country(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)

    if not author:
        raise HTTPException(status_code=404, detail=f"Author with id {author_id} does not exists")

    return author

# Book ---------------------------------------------


@app.get("/books/", response_model=list[schemas.BookSchema])
def get_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books
    

@app.get("/books/{book_id}", response_model=schemas.BookSchema)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} does not exists")

    return book

# Ticket -------------------------------------------


@app.get("/tickets/", response_model=list[schemas.TicketSchema])
def get_tickets(db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db)
    return tickets
    

@app.get("/tickets/{ticket_id}", response_model=schemas.TicketSchema)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail=f"Ticket with id {ticket_id} does not exists")

    return ticket

# User ---------------------------------------------


@app.get("/users/", response_model=list[schemas.UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users
    

@app.get("/users/{user_id}", response_model=schemas.UserSchema)
def get_ticket(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} does not exists")

    return user
