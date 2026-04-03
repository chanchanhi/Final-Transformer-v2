import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# ✅ Final-transformer-v2 디렉터리를 기준으로 .env 파일 로드
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 파일 위치 (backend/app)
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../"))  # Final-transformer-v2 디렉토리
ENV_PATH = os.path.join(ROOT_DIR, ".env")  # ✅ 최상위 디렉토리의 .env 경로

# 환경 변수 로드
load_dotenv(dotenv_path=ENV_PATH)

# 환경 변수에서 MySQL 접속 정보 가져오기
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# MySQL 연결 URL 생성
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 모델 정의
Base = declarative_base()

# 데이터베이스 연결 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
