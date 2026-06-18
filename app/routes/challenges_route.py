from app.database import get_db
from fastapi import Depends,APIRouter
from app import crud,schemas
from sqlalchemy.orm import Session
from app.auth.oauth2 import get_current_user
from app.models.user_model import User
from fastapi import Query

router=APIRouter(tags=["Challenges"])

@router.post("/learning_challenges",response_model=schemas.challenges_schema.LearningChallengeResponse)
def add_learningChallenges(challenge:schemas.challenges_schema.LearningChallengeCreate,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.challenges_crud.add_learnChallenge(challenge,current_user.id,db)

@router.post("/habit_challenges",response_model=schemas.challenges_schema.HabitChallengeResponse)
def add_habitChallenges(challenge:schemas.challenges_schema.HabitChallengeCreate,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.challenges_crud.add_habitChallenge(challenge,current_user.id,db)

@router.get("/challenges")
def get_AllChallenges(current_user: User = Depends(get_current_user),db:Session=Depends(get_db),page:int=1,limit:int=10,challenge_type:str|None=None,search:str|None=None):
    return crud.challenges_crud.getall_challenges(current_user.id,db,page,limit,challenge_type,search)

@router.get("/challenges/{id}")
def getChallengeById(id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.challenges_crud.get_challengeById(id,current_user.id,db)

@router.put("/challenges/{id}")
def update_challenges(id:int,challenge:schemas.challenges_schema.ChallengeUpdate,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.challenges_crud.update_challenge(id,challenge,current_user.id,db)

@router.delete("/challenges/{id}")
def delete_challenge(id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.challenges_crud.delete_challenge(id,current_user.id,db)