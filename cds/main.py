from fastapi import FastAPI

from cds.database import create_data, create_db_and_tables, drop_all_tables
from cds.api.openapi import custom_openapi
from cds.api.routes import dev_route, challenge_route


app = FastAPI()

@app.on_event('startup')
def on_startup():
    drop_all_tables()
    create_db_and_tables()
    create_data()
    pass

@app.on_event('shutdown')
def on_shutdown():
    drop_all_tables()
    pass

app.openapi = custom_openapi(app)

app.include_router(dev_route, tags=['Developer'])
app.include_router(challenge_route, tags=['Challenge'])
