from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import UserRegisterRequest, UserRegisterResponse
# Нужно сделать from app.api.deps.db import get_db
from app.services.registration_service import register_user

router = APIRouter()

@router.post("/register", response_model=UserRegisterResponse)
def register(data: UserRegisterRequest, db: Session = Depends(get_db)):
    try:
        register_user(data.email, data.password, db)
        return {"message": "Email has been send."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
