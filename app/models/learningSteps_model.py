from sqlalchemy import Integer,String,Column,ForeignKey,Enum
from app.database import Base
from sqlalchemy.orm import relationship
from app.schemas.enums import ChallengeStatus
from sqlalchemy import DateTime
from datetime import datetime,timezone

class Topics(Base):
    __tablename__="topics"
    id=Column(Integer,primary_key=True,index=True)
    challenge_id=Column(Integer,ForeignKey("challenges.id"))
    title=Column(String)
    status=Column(Enum(ChallengeStatus))
    learningChallenge=relationship("Challenges",back_populates="topics")
    created_at = Column(
    DateTime,
    default=datetime.now(timezone.utc))

    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )