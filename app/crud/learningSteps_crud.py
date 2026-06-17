# create,read all,read by id,update,delete
from sqlalchemy.orm import Session
from app import models,schemas
from fastapi import HTTPException

def add_topic(topic:schemas.learningSteps_schema.createTopic,user_id:int,db:Session):
    challenge = db.query(
    models.challenges_model.Challenges).filter(
    models.challenges_model.Challenges.id == topic.challenge_id,
    models.challenges_model.Challenges.userId == user_id
    ).first()
    if not challenge:
        return "Not authorized"
    new_topic=models.learningSteps_model.Topics(**topic.model_dump())
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

def getAll_Topics(challenge_id:int,user_id: int, db: Session):
    return db.query(
        models.learningSteps_model.Topics
    ).join(
        models.challenges_model.Challenges
    ).filter(
        models.learningSteps_model.Topics.challenge_id == challenge_id,
        models.challenges_model.Challenges.userId == user_id
    ).all()

def get_topicById(challenge_id:int,topic_id:int,user_id:int,db:Session):
    accessed_topic=db.query(models.learningSteps_model.Topics).join(models.challenges_model.Challenges).filter(
    models.learningSteps_model.Topics.challenge_id==challenge_id,
    models.learningSteps_model.Topics.id==topic_id,
    models.challenges_model.Challenges.userId == user_id).first()
    if accessed_topic:
        return accessed_topic
    else:
        raise HTTPException(
            status_code=404, 
            detail="Topic not found")
    
def update_topic(topic:schemas.learningSteps_schema.topicUpdate,user_id:int,challenge_id:int,topic_id:int,db:Session):
    accessed_topic=db.query(models.learningSteps_model.Topics).join(
    models.challenges_model.Challenges).filter(
    models.learningSteps_model.Topics.challenge_id==challenge_id,    
    models.learningSteps_model.Topics.id==topic_id,
    models.challenges_model.Challenges.userId == user_id).first()
    if accessed_topic:
        update_data = topic.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(accessed_topic, key, value)
        db.commit()
        db.refresh(accessed_topic)
        return accessed_topic
    else:
        raise HTTPException(
            status_code=404, 
            detail="Topic not found")
    
def delete_topic(challenge_id:int,id:int,user_id:int,db:Session):
    accessed_topic=db.query(models.learningSteps_model.Topics).join(
    models.challenges_model.Challenges).filter(
    models.learningSteps_model.Topics.challenge_id == challenge_id,
    models.learningSteps_model.Topics.id==id,
    models.challenges_model.Challenges.userId == user_id).first()
    if accessed_topic:
        db.delete(accessed_topic)
        db.commit()
    else:
        raise HTTPException(
            status_code=404, 
            detail="Topic not found")
    