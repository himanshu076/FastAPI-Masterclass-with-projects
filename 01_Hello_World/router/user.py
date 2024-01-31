from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay

router = APIRouter(
  prefix='/user',
  tags=['user']
)

# create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)

# Read all User
@router.get('/',  response_model=list[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
  return db_user.get_all_users(db)

# Read one User
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
  return db_user.get_user(db, id)

# Update User
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
  return db_user.update_user(db, id, request)

# Delete User
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
  return db_user.delete_user(db, id)


