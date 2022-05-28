from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Relationship, Field

if TYPE_CHECKING:
    from cds.schema.tables.dev_challenge_score import DevChallengeScore


class Challenge(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    developer_scores: list['DevChallengeScore'] = Relationship(back_populates='challenge')
