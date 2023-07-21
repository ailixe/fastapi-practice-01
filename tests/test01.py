# from database import SessionLocal
# from models import Question
#
# db = SessionLocal()
#
# q = db.query(Question).all()
# # a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=datetime.now())
# # db.add(a)
# # db.commit()
from models import Question, Answer
from datetime import datetime
from database import SessionLocal
db = SessionLocal()

# q = Question(subject='pybo ?2', content='i want to know2', create_date=datetime.now())
# db.add(q)
# db.commit()


q = db.query(Question).filter(Question.id == 2).first()
print(q.subject)
# a[0].subject = "update subject !!"
# db.commit()

# a = Answer(question=q, content='답변 들어가니2', create_date=datetime.now())
# db.add(a)
# db.commit()

a = db.query(Answer).get(2)
print(a.question_id)
print(a.question.subject)
print(a.question.content)
