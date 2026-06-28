from app.AI.ai_engine import engine
from app.AI.ai_prompts import TOPICS_GENERATING_PROMPT,get_challenge_UserPrompt
from app.crud.challenges_crud import get_challengeById
from sqlalchemy.orm import Session
from app.crud.learningSteps_crud import add_AIgenerated_topics

class AI_services:
    def generate_topics(self,challenge_id:int,user_id:int,db:Session):
        challenge=get_challengeById(challenge_id,user_id,db)
        messages=[
            TOPICS_GENERATING_PROMPT,
            get_challenge_UserPrompt(challenge.title)
        ]
        raw_response=engine.chat(messages)
        return add_AIgenerated_topics(raw_response,challenge_id,user_id,db)
    
service_obj=AI_services()
