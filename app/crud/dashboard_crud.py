from sqlalchemy.orm import Session
from app import models
 

def get_dashboard(user_id:int,db:Session):
    total_challenges=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.userId==user_id).count()
    completed_challenges=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.userId==user_id,models.challenges_model.Challenges.status=="completed").count()
    learning_challenges=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.userId==user_id,models.challenges_model.Challenges.challengeType=="learning").count()
    habit_challenges=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.userId==user_id,models.challenges_model.Challenges.challengeType=="habit").count()
    return{
        "total_challenges": total_challenges,
        "completed_challenges": completed_challenges,   
        "learning_challenges": learning_challenges,
        "habit_challenges": habit_challenges
    } 