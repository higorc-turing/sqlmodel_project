from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Relationship, Field

if TYPE_CHECKING:
    from cds.schema.tables import DevChallengeScore


class Developer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str

    challenge_scores: list['DevChallengeScore'] = Relationship(back_populates='developer')
