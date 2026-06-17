# create,read all,read by id,update,delete
from sqlalchemy.orm import Session
from app import models,schemas
from fastapi import HTTPException

def add_habitLog(habitLog:schemas.habitLog_schema.createHabit,user_id:int,db:Session):
    challenge = db.query(
    models.challenges_model.Challenges).filter(
    models.challenges_model.Challenges.id == habitLog.challenge_id,
    models.challenges_model.Challenges.userId == user_id
    ).first()
    if not challenge:
        return "Not authorized"
    new_habitLog=models.habitLog_model.Habit(**habitLog.model_dump())
    db.add(new_habitLog)
    db.commit()
    db.refresh(new_habitLog)
    return new_habitLog

def getAll_habitLog(challenge_id:int,user_id:int,db:Session):
    return db.query(
        models.habitLog_model.Habit
    ).join(
        models.challenges_model.Challenges
    ).filter(
        models.habitLog_model.Habit.challenge_id == challenge_id,
        models.challenges_model.Challenges.userId == user_id
    ).all()

def get_habitLogById(challenge_id:int,id:int,user_id:int,db:Session):
    accessed_habitLog=db.query(models.habitLog_model.Habit).join(models.challenges_model.Challenges).filter(
    models.habitLog_model.Habit.challenge_id == challenge_id,
    models.habitLog_model.Habit.id==id,
    models.challenges_model.Challenges.userId == user_id).first()
    if accessed_habitLog:
        return accessed_habitLog
    else:
        raise HTTPException(
            status_code=404, 
            detail="Habit log not found")