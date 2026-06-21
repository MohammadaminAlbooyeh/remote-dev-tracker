from fastapi import APIRouter, Depends, HTTPException
from backend.api.schemas import SessionResponse, ClockInResponse, ClockOutRequest
from backend.api.dependencies import get_current_user
from backend.services.session_service import SessionService
from backend.models.database import get_db

router = APIRouter()


@router.post("/clock-in", response_model=ClockInResponse)
def clock_in(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    session = service.clock_in(current_user.id)
    return session


@router.post("/clock-out", response_model=SessionResponse)
def clock_out(payload: ClockOutRequest, current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    session = service.clock_out(current_user.id, payload.note)
    return session


@router.get("", response_model=list[SessionResponse])
def list_sessions(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    return service.get_user_sessions(current_user.id)


@router.get("/active", response_model=SessionResponse | None)
def active_session(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    return service.get_active_session(current_user.id)


@router.get("/{session_id}", response_model=SessionResponse)
def get_session(session_id: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    session = service.get_session(session_id, current_user.id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session
