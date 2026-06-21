from backend.models.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def seed():
    db = SessionLocal()
    devs = [
        {"name": "John Doe", "email": "john@example.com", "password": "password123", "hourly_rate": 25.0},
        {"name": "Maria Garcia", "email": "maria@example.com", "password": "password123", "hourly_rate": 30.0},
        {"name": "Ali Rezaei", "email": "ali@example.com", "password": "password123", "hourly_rate": 20.0},
        {"name": "Hans Mueller", "email": "hans@example.com", "password": "password123", "hourly_rate": 35.0},
    ]
    admin = db.query(User).filter(User.role == "admin").first()
    if not admin:
        admin_user = User(
            name="Admin",
            email="admin@example.com",
            password=pwd_context.hash("admin123"),
            role="admin",
            hourly_rate=0,
        )
        db.add(admin_user)
        db.commit()
    for dev in devs:
        existing = db.query(User).filter(User.email == dev["email"]).first()
        if not existing:
            user = User(
                name=dev["name"],
                email=dev["email"],
                password=pwd_context.hash(dev["password"]),
                role="dev",
                hourly_rate=dev["hourly_rate"],
            )
            db.add(user)
    db.commit()
    db.close()
    print("Seed data created successfully.")


if __name__ == "__main__":
    seed()
