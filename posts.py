from typing import List
from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
import model
import schema
from database import get_db

router = APIRouter(prefix="/posts")

@router.get("/", response_model=List[schema.CreatePost])
def get_posts(db: Session = Depends(get_db)):
    """
    Получение всех постов.
    """
    posts = db.query(model.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.CreatePost)
def create_post(post_create: schema.CreatePost, db: Session = Depends(get_db)):
    """
    Создание нового поста.
    """
    new_post = model.Post(**post_create.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
