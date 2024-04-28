from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from models import User, Note

SQLALCHEMY_DATABASE_URL = "sqlite:////Users/egorprozorov/PycharmProjects/WKTestAPI2024summer/app/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
    print("Creating table...")
    Base.metadata.create_all(bind=engine)
    print("Tables created")
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if 'users' not in tables:
        Base.metadata.create_all(engine)


def add_test_data(engine):
    # Создаем новую сессию
    with Session(engine) as session:
        # Добавляем тестового пользователя
        user1 = User(username='testuser1', hashed_password='hashedpassword1')
        user2 = User(username='testuser2', hashed_password='hashedpassword2')
        session.add(user1)
        session.add(user2)

        # Добавляем некоторые заметки
        note1 = Note(content='This is a test note 1', owner=user1)
        note2 = Note(content='This is a test note 2', owner=user1)
        note3 = Note(content='This is a test note for user 2', owner=user2)
        session.add(note1)
        session.add(note2)
        session.add(note3)

        # Сохраняем изменения в базе данных
        session.commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
