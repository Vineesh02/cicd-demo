from fastapi import FastAPI

from .routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="CI/CD Demo API")
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()

