from fastapi import APIRouter, Depends, HTTPException, status
from backend.api.schemas import UserCreate, UserLogin, TokenResponse, UserResponse
from backend.api.dependencies import get_current_user
from backend.services.auth_service import AuthService
from backend.models.database import get_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(payload: UserCreate, db=Depends(get_db)):
    service = AuthService(db)
    user = service.register(payload)
    return user


@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db=Depends(get_db)):
    service = AuthService(db)
    token = service.login(payload)
    return token


@router.post("/logout")
def logout(current_user=Depends(get_current_user)):
    return {"message": "Logged out"}


@router.get("/me", response_model=UserResponse)
def me(current_user=Depends(get_current_user)):
    return current_user
