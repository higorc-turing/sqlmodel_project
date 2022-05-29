from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, Field

from cds.schema.models import DeveloperBase

if TYPE_CHECKING:
    from cds.schema.tables import DevChallengeScore


class Developer(DeveloperBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    challenge_scores: list['DevChallengeScore'] = Relationship(back_populates='developer')
