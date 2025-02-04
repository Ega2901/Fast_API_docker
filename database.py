from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:MyBase#1270@db/dockert"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Получает сессию базы данных и закрывает ее после завершения работы.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
