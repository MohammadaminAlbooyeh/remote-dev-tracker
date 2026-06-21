from fastapi import FastAPI
from backend.api.middleware import setup_middleware
from backend.api.routes.auth import router as auth_router
from backend.api.routes.sessions import router as session_router
from backend.api.routes.developers import router as developer_router
from backend.api.routes.reports import router as report_router
from backend.api.routes.admin import router as admin_router

app = FastAPI(title="Remote Dev Tracker", version="1.0.0")

setup_middleware(app)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(session_router, prefix="/api/v1/sessions", tags=["Sessions"])
app.include_router(developer_router, prefix="/api/v1/developers", tags=["Developers"])
app.include_router(report_router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/health")
def health():
    return {"status": "ok"}
