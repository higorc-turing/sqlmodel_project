from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field


class DevChallengeScoreRead(SQLModel):
    """Base class for MCQ score reads."""
    rank_percentile: float
    passed: bool
    updated_date: datetime

class ChallengeScoreRead(DevChallengeScoreRead):
    """This MCQ score reading includes developer IDs."""
    dev_id: int

class DeveloperScoreRead(DevChallengeScoreRead):
    """This MCQ score reading includes challenge IDs."""
    challenge_id: int
