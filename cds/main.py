from fastapi import FastAPI

from cds.database import create_data, create_db_and_tables, drop_all_tables
from cds.api.openapi import custom_openapi
from cds.api.routes import dev_route, challenge_route


app = FastAPI()

@app.on_event('startup')
def on_startup():
    pass

@app.on_event('shutdown')
def on_shutdown():
    pass

app.openapi = custom_openapi(app)

app.include_router(dev_route, tags=['Developer'])
app.include_router(challenge_route, tags=['Challenge'])
