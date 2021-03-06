from typing import Optional
from fastapi import APIRouter, Depends

from sqlmodel import Session, select

from cds.schema.tables import Challenge, DevChallengeScore
from cds.schema.models import ChallengeRead, ChallengeScoreRead, DevChallengeScoreRead
from cds.database import session_maker

from cds.api.routes.developer import get_one_dev_score

challenge_route = APIRouter(prefix='/challenge')


@challenge_route.get('/', response_model=list[Challenge])
def get_challenges(session: Session = Depends(session_maker)):
    with session:
        stmt = select(Challenge)
        results = session.exec(stmt).all()
        return results

@challenge_route.get('/{challenge_id}', response_model=ChallengeRead)
def get_challenge(challenge_id: int, session: Session = Depends(session_maker)) -> Optional[ChallengeRead]:
    with session:
        stmt = select(Challenge).where(Challenge.id == challenge_id)
        result = session.exec(stmt).first()
        return ChallengeRead.from_orm(result)

@challenge_route.get('/{challenge_id}/developer/', response_model=list[ChallengeScoreRead])
def get_all_challenge_scores(challenge_id: int, session: Session = Depends(session_maker)):
    with session:
        stmt = (
            select(DevChallengeScore)
            .join(Challenge)
            .where(Challenge.id == challenge_id)
        )

        results = session.exec(stmt).all()
        return results

@challenge_route.get('/{challenge_id}/developer/{dev_id}/', response_model=DevChallengeScoreRead)
def get_one_challenge_score(challenge_id: int, dev_id: int, session: Session = Depends(session_maker)):
    return get_one_dev_score(
        dev_id=dev_id,
        challenge_id=challenge_id,
        session=session
    )
