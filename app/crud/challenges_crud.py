# create,read all,read by id,update,delete
from sqlalchemy.orm import Session
from app import models,schemas
from app.schemas.enums import ChallengeType
from fastapi import HTTPException

def add_learnChallenge(challenge:schemas.challenges_schema.LearningChallengeCreate,user_id:int,db:Session):
    challenge_data=challenge.model_dump()
    new_learnChallenge=models.challenges_model.Challenges(**challenge_data,userId=user_id)
    new_learnChallenge.challengeType=ChallengeType.learning
    db.add(new_learnChallenge)
    db.commit()
    db.refresh(new_learnChallenge)
    return new_learnChallenge

def add_habitChallenge(challenge:schemas.challenges_schema.HabitChallengeCreate,user_id:int,db:Session):
    challenge_data=challenge.model_dump()
    new_habitChallenge=models.challenges_model.Challenges(**challenge_data,userId=user_id)
    new_habitChallenge.challengeType=ChallengeType.habit
    db.add(new_habitChallenge)
    db.commit()
    db.refresh(new_habitChallenge)
    return new_habitChallenge

def getall_challenges(user_id: int,db: Session,page: int,limit: int,challenge_type: str = None,search: str = None):

    query = db.query(models.challenges_model.Challenges).filter(
        models.challenges_model.Challenges.userId == user_id
    )

    if search:
        query = query.filter(
            models.challenges_model.Challenges.title.contains(search)
        )
    if challenge_type:
        query = query.filter(
            models.challenges_model.Challenges.challengeType == challenge_type
        )
    offset = (page - 1) * limit
    challenges = query.offset(offset).limit(limit).all()
    return challenges

def get_challengeById(id:int,user_id:int,db:Session):
    accessed_challenge=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.id==id,models.challenges_model.Challenges.userId==user_id).first()
    if accessed_challenge:
        if accessed_challenge.challengeType == ChallengeType.learning:
            return schemas.challenges_schema.LearningChallengeResponse.model_validate(accessed_challenge)
        else:
            return schemas.challenges_schema.HabitChallengeResponse.model_validate(accessed_challenge)
    else:
        raise HTTPException(
            status_code=404, 
            detail="Challenge not found")
    
def update_challenge(id:int,challenge:schemas.challenges_schema.ChallengeUpdate,user_id:int,db:Session):
    accessed_challenge=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.id==id,models.challenges_model.Challenges.userId==user_id).first()
    if not accessed_challenge:
        raise HTTPException(
            status_code=404, 
            detail="Challenge not found")
    update_data = challenge.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(accessed_challenge, key, value)
    db.commit()
    db.refresh(accessed_challenge)
    return accessed_challenge
    

    
def delete_challenge(id:int,user_id:int,db:Session):
    accessed_challenge=db.query(models.challenges_model.Challenges).filter(models.challenges_model.Challenges.id==id,models.challenges_model.Challenges.userId==user_id).first()
    if accessed_challenge:
        db.delete(accessed_challenge)
        db.commit()
    else:
        raise HTTPException(
            status_code=404, 
            detail="Challenge not found")
    


