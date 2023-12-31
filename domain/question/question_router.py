from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud

# APIRouter : url 해석하여 mapping
router = APIRouter(
    prefix="/api/question",
)


@router.get("/list",
            response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    print("q list")
    _question_list = question_crud.get_question_list(db)
    return _question_list


@router.get("/detail/{question_id}",
            response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    print(f"q detail : {question_id}")
    question = question_crud.get_question(db, question_id)
    return question
