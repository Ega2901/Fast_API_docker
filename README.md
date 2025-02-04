# Fast_API_docker

---

## 🚀 FastAPI CRUD с PostgreSQL и Docker

Этот проект представляет собой REST API на FastAPI с базой данных PostgreSQL, работающий в Docker.

### 📌 Функционал
- Получение списка постов  
- Создание нового поста  
- Подключение к базе данных PostgreSQL  
- Контейнеризация с Docker  

---

## 📦 Установка и запуск

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/yourusername/fastapi-docker-crud.git
cd fastapi-docker-crud
```

### 2️⃣ Установка зависимостей
> Если не используете Docker, установите зависимости вручную:
```bash
pip install -r requirements.txt
```

### 3️⃣ Запуск в Docker
```bash
docker-compose up --build
```
> После успешного запуска сервер доступен по адресу:  
> 🔗 **http://localhost:8051**

---

## 🛠 API Эндпоинты

| Метод | Эндпоинт | Описание |
|--------|----------|------------|
| **GET** | `/` | Проверка работы сервера |
| **GET** | `/hello/{name}` | Возвращает имя, переданное в URL |
| **GET** | `/posts/` | Получение всех постов |
| **POST** | `/posts/` | Создание нового поста |

### 🔹 Пример запроса `POST /posts/`
```json
{
  "title": "Новый пост",
  "content": "Содержимое поста"
}
```

### 🔹 Пример ответа
```json
{
  "title": "Новый пост",
  "content": "Содержимое поста"
}
```

---

## ⚙️ Настройка базы данных
По умолчанию используется PostgreSQL, который запускается внутри контейнера.  
Но если хотите подключить внешний сервер, измените `DATABASE_URL` в `docker-compose.yaml`:
```yaml
environment:
  - DATABASE_URL=postgresql://username:password@localhost/db_name
```

---

## 🚀 Локальный запуск без Docker
1. Установите PostgreSQL и создайте базу данных:
```sql
CREATE DATABASE dockert;
```
2. Укажите правильный `DATABASE_URL` в `database.py`:
```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:MyBase#1270@localhost/dockert"
```
3. Запустите сервер:
```bash
uvicorn main:app --reload
```

---

## 🛠 Разработка
При изменении кода необходимо перезапустить контейнер:
```bash
docker-compose down
docker-compose up --build
```
