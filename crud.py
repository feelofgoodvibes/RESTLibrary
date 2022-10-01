from sqlalchemy.orm import Session
import schemas
from models import Genre, User, Country


def get_genres(db: Session):
    return db.query(Genre).all()

def get_countries(db: Session):
    return db.query(Country).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()