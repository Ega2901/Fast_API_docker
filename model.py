from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

class Post(Base):
    """
    Модель поста для хранения записей в базе данных.
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
