from fastapi.middleware.cors import CORSMiddleware
from backend.utils.config import settings


def setup_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
