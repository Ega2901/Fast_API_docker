from pydantic import BaseModel

class PostBase(BaseModel):
    """Базовая схема поста"""
    title: str
    content: str

    class Config:
        orm_mode = True

class CreatePost(PostBase):
    """Схема для создания поста"""
    pass
