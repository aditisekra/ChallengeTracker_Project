# create,read all,read by id,update,delete
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models,schemas
from app.auth.hashing import hash_password,verify_password

def create_user(user:schemas.user_schema.UserCreate,db:Session):
    existing_user = db.query(models.user_model.User).filter(
        models.user_model.User.email == user.email
    ).first()
    existing_username = db.query(models.user_model.User).filter(
        models.user_model.User.username == user.username
    ).first()
    if existing_username:
        raise HTTPException(
            status_code=400, 
            detail="Username already taken")
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered")
    user_data=user.model_dump()
    password=user_data.pop("password")
    hashed_password=hash_password(password)
    new_user=models.user_model.User(**user_data,password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    return new_user

def authenticate_user(user: schemas.user_schema.UserLogin, db: Session):
    userlogin = db.query(models.user_model.User).filter(
        models.user_model.User.email == user.email
    ).first()
    if not userlogin:
        return None
    if not verify_password(user.password, userlogin.password_hash):
        return None
    return userlogin
    
def update_user(user:schemas.user_schema.UserUpdate,user_id:int,db:Session):
    accessed_user=db.query(models.user_model.User).filter(models.user_model.User.id==user_id).first()
    if accessed_user:
        accessed_user.username=user.username
        db.commit()
        return accessed_user
    else:
        raise HTTPException(
            status_code=404, 
            detail="User not found")
    

def delete_user(user_id:int,db:Session):
    accessed_user=db.query(models.user_model.User).filter(models.user_model.User.id==user_id).first()
    if accessed_user:
        db.delete(accessed_user)
        db.commit()
    else:
        raise HTTPException(
            status_code=404, 
            detail="User not found")
