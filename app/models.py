from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    notes = relationship("Note", back_populates="owner")


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    date_created = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="notes")
