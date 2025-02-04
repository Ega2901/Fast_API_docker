from fastapi import FastAPI
import model
from database import engine
import posts

app = FastAPI()

# Подключаем маршрутизатор для работы с постами
app.include_router(posts.router)

# Создание таблиц в базе данных
model.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    """Корневой маршрут API"""
    return {"message": "Docker is cool"}

@app.get("/hello/{name}")
async def hello(name: str):
    """Приветственный маршрут"""
    return {"message": f"Your name: {name}"}
