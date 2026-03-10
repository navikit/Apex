from fastapi import FastAPI

from app import api, db


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Life Optimizer",
        description="An intelligent personal operating system prototype.",
        version="0.1.0",
    )

    app.include_router(api.router)

    @app.on_event("startup")
    async def startup_event():
        db.init_db()

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    return app


app = create_app()
