import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.activation_token import ActivationToken
# Нужно сделать  from app.core.security import hash_password
from app.services.email_service import send_activation_email

def register_user(email: str, password: str, db: Session):
    # 1. Проверка уникальности
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("Email уже зарегистрирован.")

    # 2. Создание пользователя
    hashed_pwd = hash_password(password)
    new_user = User(email=email, hashed_password=hashed_pwd)
    db.add(new_user)
    db.flush()  # получить ID до коммита

    # 3. Генерация токена
    token = str(uuid.uuid4())
    expires = datetime.utcnow() + timedelta(hours=24)
    activation = ActivationToken(user_id=new_user.id, token=token, expires_at=expires)
    db.add(activation)
    db.commit()

    # 4. Отправка письма
    #send_activation_email(email, token)
