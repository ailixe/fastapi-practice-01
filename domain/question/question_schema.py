import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    # 기본값 설정 : str or None - 기본 값은 None
    subject: str | None = None
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
