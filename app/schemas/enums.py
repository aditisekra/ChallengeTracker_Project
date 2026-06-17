from enum import Enum

class ChallengeStatus(str,Enum):
    completed="Complete"
    not_completed="Incomplete"
    in_progress="In Progress"

class ChallengeType(str,Enum):
    learning="Learning Challenge"
    habit="Habit Challenge"