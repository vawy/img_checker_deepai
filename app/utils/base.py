from fastapi import APIRouter, FastAPI


def bind_routes(app: FastAPI, routes: list[APIRouter]):
    for route in routes:
        app.include_router(route, prefix="/api/image_editor")
