from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field


class DevChallengeScoreRead(SQLModel):
    """Base class for MCQ score reads."""
    rank_percentile: float
    passed: bool
    updated_date: datetime

class ChallengeScoreRead(DevChallengeScoreRead):
    """This data model will include developer ID in a list of scores."""
    dev_id: int

class DeveloperScoreRead(DevChallengeScoreRead):
    """This data model will include challenge ID in a list of scores."""
    challenge_id: int
