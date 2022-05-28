from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi

from cds.api.routes import dev_route, challenge_route
from cds.database import create_data, create_db_and_tables, drop_all_tables


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

def custom_openapi() -> dict:
    """This function creates a custom OpenAPI json.

    Returns:
        dict: Stores the custom OpenAPI json.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Turing Centralized Data Service",
        version="0.1.0",
        description="Turing's one-stop-shop for common product KPIs.",
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title": "Turing Centralized Data Service",
        "description": "Turing's one-stop-shop for common product KPIs.",
        "version": "0.1.0",
        "x-logo": {"url": "https://www.turing.com/img/header-logo01.svg"},
    }
    openapi_schema["tags"] = [
        {"name": "Developer", "description": "This route provides data about developers."},
        {"name": "Challenge", "description": "This route provides data about challenges."},
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


app.include_router(dev_route, tags=['Developer'])
app.include_router(challenge_route, tags=['Challenge'])
