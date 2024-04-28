from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import User, Note, Base

SQLALCHEMY_DATABASE_URL = "sqlite:////Users/egorprozorov/PycharmProjects/WKTestAPI2024summer/app/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    print("Creating tables...")
    try:
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", e)


def add_test_data(engin):
    # Создаем новую сессию
    with Session(engin) as session:
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
