from fastapi import APIRouter, Depends
from backend.api.schemas import UserResponse
from backend.api.dependencies import get_current_user
from backend.models.database import get_db
from backend.services.auth_service import AuthService

router = APIRouter()


@router.get("/profile", response_model=UserResponse)
def profile(current_user=Depends(get_current_user)):
    return current_user


@router.put("/profile", response_model=UserResponse)
def update_profile(payload: dict, current_user=Depends(get_current_user), db=Depends(get_db)):
    service = AuthService(db)
    user = service.update_profile(current_user.id, payload)
    return user
