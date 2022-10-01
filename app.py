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


@app.get("/users/", response_model=list[schemas.UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/genres/", response_model=list[schemas.Genre])
def get_genres(db: Session = Depends(get_db)):
    genres = crud.get_genres(db)
    return genres