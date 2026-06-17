from pydantic import BaseModel

class DashboardSummary(BaseModel):
    total_challenges: int
    learning_challenges: int
    habit_challenges: int
    completed_topics: int
    total_topics: int
    habit_logs: int