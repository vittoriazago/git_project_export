from fastapi import FastAPI


def configure_routes(app: FastAPI):
    from app.rest.projects_rest import router as project_rest_router

    routers = (
        project_rest_router,
    )

    for route in routers:
        app.include_router(route)
