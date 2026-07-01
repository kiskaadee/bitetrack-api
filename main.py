from fastapi import FastAPI

from routers import router, system_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(system_router, tags=["System Info"])
    app.include_router(router, prefix="/api/v2", tags=["BiteTrack v2"])

    return app


app = create_app()
