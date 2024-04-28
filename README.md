
# Project Name: Тестовое задания для VK API

## Описание
Этот проект представляет собой простой REST API, разработанный с использованием FastAPI. Он позволяет пользователям регистрироваться, входить в систему и управлять заметками. Пользователи могут создавать, просматривать и удалять заметки.

## Технологический стек
- **FastAPI**: Асинхронный фреймворк для построения REST API.
- **SQLAlchemy**: ORM для взаимодействия с базами данных.
- **SQLite**: Легковесная база данных для хранения данных пользователя и заметок.
- **Pydantic**: Библиотека для валидации данных и управления настройками на основе моделей Python.

## Установка и настройка
Чтобы начать работу, клонируйте репозиторий и установите зависимости:
```bash
git clone https://github.com/EgorProzorov/VKTestAPI2024summer
cd VKTestAPI2024summer
pip install -r requirements.txt
```

## Использование API
### Swagger
Вы можете посмотреть все ручки апи, с помощью Swagger, он доступен по ендпоинту `/docs`   
### Регистрация пользователя
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

### Вход пользователя
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/token' \
  -d 'username=your_username&password=your_password'
```

### Добавление заметки
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/notes/' \
  -H 'Authorization: Bearer your_token' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Note Title",
  "content": "Content of your note"
}'
```

## Запуск проекта
Перейдите в папку *app* и выполните команду:
```bash
uvicorn main:app --reload
```
