from sqlalchemy import Date,String,Integer,Column,ForeignKey,Enum
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from datetime import datetime,timezone
from app.schemas.enums import ChallengeStatus,ChallengeType

# not completed yet

class Challenges(Base):
    __tablename__="challenges"
    id=Column(Integer,primary_key=True,index=True)
    userId=Column(Integer,ForeignKey("users.id"))
    title=Column(String)
    description=Column(String)
    challengeType=Column(Enum(ChallengeType))
    start_date=Column(Date,nullable=False)
    end_date=Column(Date,nullable=True)
    status=Column(Enum(ChallengeStatus))
    topics=relationship("Topics",back_populates="learningChallenge",cascade="all,delete")
    habits=relationship("Habit",back_populates="habitChallenge",cascade="all,delete")
    user=relationship("User",back_populates="challenges")
    created_at = Column(
    DateTime,
    default=datetime.now(timezone.utc))

    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )