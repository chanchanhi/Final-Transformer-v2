from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import app.models as models
from app.routes import users
from app.database import engine, get_db

# 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 사용자 API 추가
app.include_router(users.router, prefix="/users", tags=["Users"])

# 데이터베이스 연결 테스트
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "Database connected"}
