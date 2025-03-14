from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User 데이터 검증용 Pydantic 모델
class UserCreate(BaseModel):
    google_id: str
    email: EmailStr
    name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    google_id: str
    email: EmailStr
    name: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
