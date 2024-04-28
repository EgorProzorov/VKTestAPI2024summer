from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from .models import User, Note

# Строка подключения к базе данных
# Пример использования SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Для PostgreSQL использование будет выглядеть примерно так:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Только для SQLite; уберите для других СУБД
)

# Сессия для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()


def init_db():
    """Инициализирует базу данных, создавая все таблицы."""
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)  # Создание таблиц
    add_test_data(engine)


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
    """Генератор, предоставляющий сессию базы данных и обеспечивающий её закрытие после использования."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
