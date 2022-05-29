from typing import Optional
from fastapi import APIRouter, Depends

from sqlmodel import Session, select

from cds.schema.tables import Developer, Challenge, DevChallengeScore
from cds.schema.models import DeveloperScoreRead, DevChallengeScoreRead, DeveloperRead
from cds.database import session_maker

dev_route = APIRouter(prefix='/developer')


@dev_route.get('/', response_model=list[Developer])
def get_developers(session: Session = Depends(session_maker)) -> list[Developer]:
    with session:
        stmt = select(Developer)
        results = session.exec(stmt).all()
        return results

@dev_route.get('/{dev_id}/', response_model=DeveloperRead)
def get_developer(dev_id: int, session: Session = Depends(session_maker)) -> Optional[DeveloperRead]:
    with session:
        stmt = select(Developer).where(Developer.id == dev_id)
        result = session.exec(stmt).first()
        return DeveloperRead.from_orm(result)

@dev_route.get('/{dev_id}/challenge/', response_model=list[DeveloperScoreRead])
def get_all_dev_scores(dev_id: int, session: Session = Depends(session_maker)) -> list[DeveloperScoreRead]:
    with session:
        stmt = (
            select(DevChallengeScore)
            .join(Developer)
            .join(Challenge)
            .where(Developer.id == dev_id)
        )

        results = session.exec(stmt).all()
        return [DeveloperScoreRead.from_orm(item) for item in results]

@dev_route.get('/{dev_id}/challenge/{challenge_id}/', response_model=DevChallengeScoreRead)
def get_one_dev_score(dev_id: int, challenge_id: int, session: Session = Depends(session_maker)) -> Optional[DevChallengeScoreRead]:
    with session:
        stmt = (
            select(DevChallengeScore)
            .join(Developer)
            .join(Challenge)
            .where(Developer.id == dev_id)
            .where(Challenge.id == challenge_id)
        )

        result = session.exec(stmt).first()
        return result
