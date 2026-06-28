from pydantic import BaseModel,Field
from typing import List,Optional
from datetime import date
from app.schemas.enums import ChallengeStatus
from app.schemas import learningSteps_schema, habitLog_schema

class ChallengeBase(BaseModel):
    title: str=Field(min_length=3,max_length=30)
    description: str=Field(min_length=3,max_length=40)
    start_date: date
    end_date: Optional[date] = None
    status: ChallengeStatus

class LearningChallengeCreate(ChallengeBase):
    pass

class HabitChallengeCreate(ChallengeBase):
    pass

class ChallengeUpdate(BaseModel):
    title: str | None = Field(default=None,min_length=3,max_length=30)
    description: str | None = Field(default=None,min_length=3,max_length=40)
    end_date: Optional[date] = None
    status: Optional[ChallengeStatus] = None

class LearningChallengeResponse(ChallengeBase):
    id: int
    userId: int
    title: str | None = Field(default=None,min_length=3,max_length=30)
    topics: List[
        learningSteps_schema.TopicsBase
    ] = Field(default_factory=list)
    class Config:
        from_attributes = True

class HabitChallengeResponse(ChallengeBase):
    id: int
    userId: int
    habits: List[
        habitLog_schema.HabitBase
    ] = Field(default_factory=list)
    class Config:
        from_attributes = True
