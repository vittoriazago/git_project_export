from fastapi import FastAPI

from app.config.router_config import configure_routes


def configure_fast_api(app: FastAPI):
    configure_routes(app)
