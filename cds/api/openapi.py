from typing import Callable

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

def custom_openapi(app: FastAPI) -> Callable:
    def openapi() -> dict:
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

    return openapi
