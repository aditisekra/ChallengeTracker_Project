from pydantic import BaseModel,Field
from app.schemas.enums import ChallengeStatus

class TopicsBase(BaseModel):
    challenge_id:int
    title:str=Field(min_length=3,max_length=30)
    status:ChallengeStatus
    class Config:
        from_attributes=True

class createTopic(TopicsBase):
    pass

class topicResponse(TopicsBase):
    pass

class topicUpdate(BaseModel):
    title:str=Field(min_length=3,max_length=30)
    status:ChallengeStatus
