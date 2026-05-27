from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import RedirectResponse
from app.services.mqtt_service import connect_mqtt

from app.api.routes import device



def create_app() -> FastAPI:
    """Create and configure FastAPI application.
    """
    app = FastAPI(title="NodeAI Backend", version="0.1.0")

    # Basic CORS for development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(device.router)

    @app.on_event("startup")
    def startup_event():
        connect_mqtt()

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse("/docs")

    @app.get("/healthz", tags=["health"])
    def health() -> dict:
        return {"status": "ok"}

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
