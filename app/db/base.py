from app.models.user import User
from app.models.user_group import UserGroup
from app.models.tokens import ActivationToken, PasswordResetToken, RefreshToken
from app.models.user_profile import UserProfile


from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
