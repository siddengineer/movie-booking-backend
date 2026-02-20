from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import User, Booking, Show, Screen, Theater, Movie
from passlib.context import CryptContext

# Hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin(db: Session):
    admin_email = "admin@example.com"
    admin_username = "admin"
    admin_password = "admin123"  # Change if you want a stronger password

    # Check if admin already exists
    existing_admin = db.query(User).filter(User.is_admin == 1).first()
    if existing_admin:
        print("Admin already exists, updating password...")
        existing_admin.password = pwd_context.hash(admin_password)
        db.commit()
        print(f"Admin {admin_email} password updated!")
        return

    hashed_password = pwd_context.hash(admin_password)
    new_admin = User(
        username=admin_username,
        email=admin_email,
        password=hashed_password,
        is_admin=1
    )
    db.add(new_admin)
    db.commit()
    print(f"Admin {admin_email} created successfully!")

if __name__ == "__main__":
    db = next(get_db())
    create_admin(db)