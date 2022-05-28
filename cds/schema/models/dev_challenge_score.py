from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field


class DevChallengeScoreRead(SQLModel):
    rank_percentile: float
    passed: bool
    updated_date: datetime
