from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    date_created: datetime
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
