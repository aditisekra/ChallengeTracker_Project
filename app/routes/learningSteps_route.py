from fastapi import Depends,APIRouter
from app import schemas,crud
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.oauth2 import get_current_user
from app.models.user_model import User

router=APIRouter(tags=["Topics"])

@router.post("/topics")
def add_topic(topic:schemas.learningSteps_schema.createTopic,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.learningSteps_crud.add_topic(topic,current_user.id,db)

@router.get("/topics/{challenge_id}")
def get_allTopics(challenge_id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.learningSteps_crud.getAll_Topics(challenge_id,current_user.id,db)

@router.get("/challenge/{challenge_id}/topics/{topic_id}")
def getTopicById(challenge_id:int,topic_id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.learningSteps_crud.get_topicById(challenge_id,topic_id,current_user.id,db)

@router.put("/challenge/{challenge_id}/topics/{topic_id}")
def update_topic(topic:schemas.learningSteps_schema.topicUpdate,challenge_id:int,topic_id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.learningSteps_crud.update_topic(topic,current_user.id,challenge_id,topic_id,db)

@router.delete("/topics/{id}")
def delete_topic(challenge_id:int,id:int,current_user: User = Depends(get_current_user),db:Session=Depends(get_db)):
    return crud.learningSteps_crud.delete_topic(challenge_id,id,current_user.id,db)
