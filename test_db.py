# from app.core.database import engine
# from app.models.movie import Movie
# from app.models.theater import Theater
# from app.models.screen import Screen
# from app.models.show import Show
# from app.models.user import User

# print("Models imported successfully")
from app.core.database import Base, engine
from app.models.show import Show
from app.models.screen import Screen
from app.models.movie import Movie
from app.models.theater import Theater
from app.models.user import User
from app.models.booking import Booking

# Try creating all tables / check ORM
Base.metadata.create_all(bind=engine)
print("✅ ORM relationships fixed")
