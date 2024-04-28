from sqlalchemy.orm import Session

import schemas
import models
from models import User
from passlib.context import CryptContext


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_note(db: Session, note: schemas.NoteCreate, user_id: int):
    db_note = models.Note(title=note.title, content=note.content, owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()
