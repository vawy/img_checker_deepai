import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI

from app.utils.base import bind_routes
from app.handlers import routes
from app.settings import Settings, settings


def make_app(app_settings: Settings) -> FastAPI:
    fastapi_app = FastAPI(
        title="Image editor",
        docs_url="/api/images_editor/swagger"
    )
    bind_routes(app=fastapi_app, routes=routes)

    return fastapi_app


if __name__ == "__main__":
    uvicorn.run(app=make_app(app_settings=settings))
