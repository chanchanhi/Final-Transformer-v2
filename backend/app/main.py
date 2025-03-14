from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import engine, get_db

# 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 데이터베이스 연결 테스트
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "Database connected"}
