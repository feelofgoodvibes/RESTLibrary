from typing import final
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


@app.get("/countries/", response_model=list[schemas.Country])
def get_countries(db: Session = Depends(get_db)):
    countries = crud.get_countries(db)
    return countries


@app.get("/genres/", response_model=list[schemas.Genre])
def get_genres(db: Session = Depends(get_db)):
    genres = crud.get_genres(db)
    return genres


@app.get("/authors/", response_model=list[schemas.AuthorSchema])
def get_genres(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return authors


@app.get("/books/", response_model=list[schemas.BookSchema])
def get_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books



@app.get("/tickets/", response_model=list[schemas.TicketSchema])
def get_tickets(db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db)
    return tickets


@app.get("/users/", response_model=list[schemas.UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users
