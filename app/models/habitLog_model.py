from app.database import Base
from sqlalchemy import Column,Integer,String,Date,DateTime,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from datetime import datetime,timezone

class Habit(Base):
    __tablename__="habits"
    id=Column(Integer,primary_key=True,index=True)
    challenge_id=Column(Integer,ForeignKey("challenges.id"))
    date=Column(DateTime, default=datetime.now)
    habitChallenge=relationship("Challenges",back_populates="habits")
    created_at = Column(
    DateTime,
    default=datetime.now(timezone.utc))

    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )