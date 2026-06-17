from pydantic import BaseModel
from datetime import date

class HabitBase(BaseModel):
    challenge_id:int
    date:date
    class Config:
        from_attributes=True

class createHabit(HabitBase):
    pass

class HabitLogResponse(HabitBase):
    pass