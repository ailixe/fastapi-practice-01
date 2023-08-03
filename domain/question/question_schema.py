import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer


class Question(BaseModel):
    id: int
    # 기본값 설정 : str or None - 기본 값은 None
    subject: str | None = None
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        from_attributes = True
