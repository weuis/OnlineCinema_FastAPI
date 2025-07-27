from pydantic import BaseModel

class ActivationTokenOut(BaseModel):
    token: str
    expires_at: str

    class Config:
        orm_mode = True