from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.database import get_db
from app import crud
from app.auth.oauth2 import get_current_user

router=APIRouter(tags=["Dashboard"])

@router.get("/dashboard")
def get_dashboard(current_user: User = Depends(get_current_user),db:Session=Depends(get_db)): 
    return crud.dashboard_crud.get_dashboard(current_user.id,db)
    