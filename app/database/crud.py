from . import schemas, models

from sqlalchemy.orm import Session
from typing import Union, List, Type


def get_tests(session: Session, limit: Union[int, None] = None) -> Union[List[Type[models.Test]], None]:
    result = session.query(models.Test)
    if limit:
        return result.limit(limit).all()
    return result.all()


def get_test_by_id(uid: int, session: Session) -> Union[models.Test, None]:
    return session.get(models.Test, uid)


def get_answer(uid_test: int, uid_quest, session: Session):
    return get_test_by_id(uid=uid_test, session=session).quests


# This function create and commit test into database
def create_test(
        session: Session,
        test: schemas.Test,
        questions: List[schemas.QuestionNew]
        ):
    test = models.Test(**test.model_dump())
    test.quests = [models.Question(**i.model_dump()) for i in questions]
    session.add(test)
    session.commit()
