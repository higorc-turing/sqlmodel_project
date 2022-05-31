from typing import Optional
from datetime import datetime
from sqlmodel import Relationship, Field

from cds.schema.tables import Developer, Challenge
from cds.schema.models import DevChallengeScoreRead


class DevChallengeScore(DevChallengeScoreRead, table=True):
    __tablename__: str = 'developer_mcq_score'

    dev_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='developer.id')
    challenge_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='challenge.id')

    developer: Developer = Relationship(back_populates='challenge_scores')
    challenge: Challenge = Relationship(back_populates='developer_scores')
