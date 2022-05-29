from sqlmodel import SQLModel


class ChallengeBase(SQLModel):
    name: str

class ChallengeRead(ChallengeBase):
    pass
