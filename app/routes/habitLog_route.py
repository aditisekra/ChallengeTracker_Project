from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter
from app import crud,schemas
from app.database import get_db
from app.auth.oauth2 import get_current_user
from app.models.user_model import User

router=APIRouter(tags=["HabitLog"])

@router.post("/habit")
def add_habitLog(habit:schemas.habitLog_schema.createHabit,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.habitLog_crud.add_habitLog(habit,current_user.id,db)

@router.get("/habit")
def get_AllHabitLogs(challenge_id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.habitLog_crud.getAll_habitLog(challenge_id,current_user.id,db)

@router.get("/habit/{id}")
def getHabitLogById(challenge_id:int,id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.habitLog_crud.get_habitLogById(challenge_id,id,current_user.id,db)