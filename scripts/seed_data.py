from backend.models.database import SessionLocal
from backend.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def seed():
    db = SessionLocal()
    devs = [
        {"name": "Dev One", "email": "dev1@example.com", "password": "dev1", "hourly_rate": 25.0},
        {"name": "Dev Two", "email": "dev2@example.com", "password": "dev2", "hourly_rate": 30.0},
        {"name": "Dev Three", "email": "dev3@example.com", "password": "dev3", "hourly_rate": 20.0},
    ]
    admin = db.query(User).filter(User.role == "admin").first()
    if not admin:
        admin_user = User(
            name="Admin",
            email="admin@example.com",
            password=pwd_context.hash("admin"),
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
