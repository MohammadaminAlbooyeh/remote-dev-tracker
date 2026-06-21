from backend.models.database import engine, Base
from backend.models.user import User
from backend.models.session import Session


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()
