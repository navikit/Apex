from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app import api, db


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Life Optimizer",
        description="An intelligent personal operating system prototype.",
        version="0.1.0",
    )

    app.include_router(api.router)

    # Serve the simple web UI from the `web/` folder.
    web_root = Path(__file__).resolve().parent.parent / "web"
    app.mount("/", StaticFiles(directory=web_root, html=True), name="web")

    @app.on_event("startup")
    async def startup_event():
        db.init_db()

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    return app


app = create_app()
