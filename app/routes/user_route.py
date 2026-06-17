from app.database import get_db
from fastapi import Depends,APIRouter,HTTPException
from app import crud,schemas
from sqlalchemy.orm import Session
from app.auth.oauth2 import get_current_user
from app.models.user_model import User

router=APIRouter(tags=["Me"])

@router.put("/me/{id}")
def update_user(user:schemas.user_schema.UserUpdate,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.user_crud.update_user(user,current_user.id,db)

@router.delete("/me/{id}")
def delete_user(current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.user_crud.delete_user(current_user.id,db)

