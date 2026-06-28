from app.database import get_db
from fastapi import Depends,APIRouter
from app import crud,schemas
from app.services import ai_services
from sqlalchemy.orm import Session
from app.auth.oauth2 import get_current_user
from app.models.user_model import User


router=APIRouter(tags=["AI"])

@router.post("/ai/{challenge_id}")
def generate_AItopics(challenge_id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return ai_services.service_obj.generate_topics(challenge_id,current_user.id,db)
