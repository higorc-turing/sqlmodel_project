from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field


class DevChallengeScoreRead(SQLModel):
    """Base class for MCQ score reads."""
    rank_percentile: float = Field(nullable=False)
    passed: bool = Field(nullable=False)
    updated_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class ChallengeScoreRead(DevChallengeScoreRead):
    """This MCQ score reading includes developer IDs."""
    dev_id: int

class DeveloperScoreRead(DevChallengeScoreRead):
    """This MCQ score reading includes challenge IDs."""
    challenge_id: int
