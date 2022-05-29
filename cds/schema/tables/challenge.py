from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, Field

from cds.schema.models import ChallengeBase

if TYPE_CHECKING:
    from cds.schema.tables.dev_challenge_score import DevChallengeScore


class Challenge(ChallengeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    developer_scores: list['DevChallengeScore'] = Relationship(back_populates='challenge')
