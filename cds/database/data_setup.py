from sqlmodel import SQLModel

from .config import engine, session_maker

from cds.schema.tables import Developer, Challenge, DevChallengeScore

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_data():
    with session_maker() as session:
        higor = Developer(name="Higor", country="Brazil")
        rehman = Developer(name="Rehman", country="Pakistan")
        ivan = Developer(name="Ivan", country="Anywhere but Russia")

        ml_mcq = Challenge(name='Machine Learning')
        sw_mcq = Challenge(name='Software Engineering')
        tb_mcq = Challenge(name='Team Building')

        submissions: list = [
            DevChallengeScore(developer=higor, challenge=ml_mcq, rank_percentile=.9, passed=True),
            DevChallengeScore(developer=higor, challenge=sw_mcq, rank_percentile=.35, passed=True),
            DevChallengeScore(developer=higor, challenge=tb_mcq, rank_percentile=.2, passed=False),

            DevChallengeScore(developer=rehman, challenge=ml_mcq, rank_percentile=1, passed=True),
            DevChallengeScore(developer=rehman, challenge=sw_mcq, rank_percentile=.7, passed=True),
            DevChallengeScore(developer=rehman, challenge=tb_mcq, rank_percentile=.5, passed=True),

            DevChallengeScore(developer=ivan, challenge=ml_mcq, rank_percentile=.9, passed=True),
            DevChallengeScore(developer=ivan, challenge=sw_mcq, rank_percentile=.75, passed=True),
            DevChallengeScore(developer=ivan, challenge=tb_mcq, rank_percentile=.8, passed=True),
        ]

        for sub in submissions:
            session.add(sub)

        session.commit()

def drop_all_tables():
    SQLModel.metadata.drop_all(engine)
