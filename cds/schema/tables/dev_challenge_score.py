from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Relationship, Field

from cds.schema.tables import Developer, Challenge
from cds.schema.models import DevChallengeScoreRead


class DevChallengeScore(DevChallengeScoreRead, table=True):
    dev_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='developer.id')
    challenge_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='challenge.id')
    rank_percentile: float
    passed: bool
    updated_date: datetime = Field(default_factory=datetime.utcnow)

    developer: Developer = Relationship(back_populates='challenge_scores')
    challenge: Challenge = Relationship(back_populates='developer_scores')
