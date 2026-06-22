from passlib.context import CryptContext
from jose import jwt, JWTError
from backend.models.user import User
from backend.utils.config import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, db):
        self.db = db

    def register(self, payload):
        existing = self.db.query(User).filter(User.email == payload.email).first()
        if existing:
            raise ValueError("Email already registered")
        hashed = pwd_context.hash(payload.password)
        user = User(
            name=payload.name,
            email=payload.email,
            password=hashed,
            hourly_rate=payload.hourly_rate,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def login(self, payload):
        user = self.db.query(User).filter(User.email == payload.email).first()
        if not user or not pwd_context.verify(payload.password, user.password):
            raise ValueError("Invalid credentials")
        if not user.is_active:
            raise ValueError("Account is deactivated")
        token = self._create_token(user)
        return {"access_token": token, "token_type": "bearer"}

    def verify_token(self, token: str):
        try:
            data = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            user_id = data.get("sub")
            if not user_id:
                return None
            return self.db.query(User).filter(User.id == user_id).first()
        except JWTError:
            return None

    def get_all_developers(self, skip: int = 0, limit: int = 100):
        return (
            self.db.query(User)
            .filter(User.role == "dev")
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update_profile(self, user_id: str, payload: dict):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        for key, value in payload.items():
            if hasattr(user, key):
                setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def deactivate(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.is_active = False
            self.db.commit()

    def _create_token(self, user: User) -> str:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        data = {"sub": user.id, "email": user.email, "role": user.role}
        data.update({"exp": expire})
        return jwt.encode(data, settings.secret_key, algorithm=settings.algorithm)
