from fastapi import FastAPI

from routers import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router, prefix="/api/v2", tags=["BiteTrack V2"])

    return app


app = create_app()
