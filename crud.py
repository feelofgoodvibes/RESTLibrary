from sqlalchemy.orm import Session
from models import Genre, User, Country, Author, Book, Ticket
from schemas import genre, user, country, author, book, ticket


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

def get_collection(db: Session, collection_class, limit: int = None, offset: int = None):
    '''A uniform method to get all items in collection (all rows of model)'''
    return db.query(collection_class).limit(limit).offset(offset).all()


def get_collection_item(db: Session, collection_class, primary_key_field, pk_value):
    '''A uniform method to get item of collection by it's primary value'''
    return db.query(collection_class).filter(primary_key_field == pk_value).first()


def create_country(country: country.CountryCreate, db: Session):
    new_country = Country(name=country.name)

    db.add(new_country)
    db.commit()
    db.refresh(new_country)

    return new_country
