from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 로컬 저장
SQLALCHEMY_DATABASE_URL = "sqlite:///E:\\ml-projects\\fastapi-practice\\myapi.db"

# 커넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# db 접속 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# model 구성시 사용
Base = declarative_base()


def get_db():
    print("get db start")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
