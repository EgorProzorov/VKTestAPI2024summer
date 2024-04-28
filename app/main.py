from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import auth, crud, database, models, schemas
from .database import init_db
# import crud
# import database
# import models
# import schemas

app = FastAPI()

print("Initializing database...")
init_db()
print("Database tables created.")
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Проверяем, существует ли уже пользователь с таким именем
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # Если пользователя нет, создаем нового с хэшированным паролем
    return crud.create_user(db=db, user=user)


@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_note(db=db, note=note, user_id=current_user.id)


@app.get("/notes/", response_model=list[schemas.Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db),
               current_user: models.User = Depends(auth.get_current_user)):
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes