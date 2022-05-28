from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from cds.api.routes import dev_route, challenge_route
from cds.database import get_session

from cds.schema.tables import Developer, Challenge, DevChallengeScore
from cds.schema.models import DevChallengeScoreRead


app = FastAPI()

@app.on_event('startup')
def on_startup():
    # drop_all_tables()
    # create_db_and_tables()
    # create_data()
    pass

@app.on_event('shutdown')
def on_shutdown():
    # drop_all_tables()
    pass

app.include_router(dev_route)
app.include_router(challenge_route)
