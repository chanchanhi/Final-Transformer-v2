from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy Base 설정
Base = declarative_base()

# 사용자 테이블 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    google_id = Column(String(255), unique=True, nullable=False)  # 구글 로그인 ID
    email = Column(String(255), unique=True, nullable=False)  # 사용자 이메일
    name = Column(String(255))  # 사용자 이름
    created_at = Column(TIMESTAMP, default=func.now())  # 계정 생성 날짜
