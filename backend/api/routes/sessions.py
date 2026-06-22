from fastapi import APIRouter, Depends, HTTPException, status, Query
from backend.api.schemas import SessionResponse, ClockInResponse, ClockOutRequest
from backend.api.dependencies import get_current_user
from backend.services.session_service import SessionService
from backend.models.database import get_db

router = APIRouter()


@router.post("/clock-in", response_model=ClockInResponse)
def clock_in(current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    try:
        session = service.clock_in(current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return session


@router.post("/clock-out", response_model=SessionResponse)
def clock_out(payload: ClockOutRequest, current_user=Depends(get_current_user), db=Depends(get_db)):
    service = SessionService(db)
    try:
        session = service.clock_out(current_user.id, payload.note)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return session


@router.get("", response_model=list[SessionResponse])
def list_sessions(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    service = SessionService(db)
    return service.get_user_sessions(current_user.id, skip, limit)


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
