from . import schemas, models
from sqlalchemy import select, Row, delete
from sqlalchemy.orm import Session
from typing import Union, List, Type, Tuple, Sequence, Optional

from .models import Test, Question

"""
    Этот файл нужен для работы с базой данных и преобразования ответов моделей в pydantic модели. Валидация и защита от 
    sql injections делается в main ...
"""


def get_tests(session: Session, limit: Union[int, None] = 10) -> Sequence[Row[tuple[Test]]]:
    query = select(models.Test)
    if limit:
        query = query.limit(limit)
    return session.execute(query).all()


def get_test_by_id(uid_test: int, session: Session) -> Optional[models.Test]:
    return session.get(models.Test, uid_test)


def get_questions(test_id: int, session: Session) -> Optional[Question]:
    test = get_test_by_id(test_id, session)
    if test:
        return test.quests
    return None


def get_answers(uid_test: int, uid_quest: int, session: Session) -> Optional[List[str]]:
    """
    :param uid_test: id of test
    :param uid_quest: id of question pin on test
    :param session: session for work with orm models from sqlalchemy
    :return: list of answers or None
    """
    query = select(models.Question) \
        .where(models.Question.test_id == uid_test, models.Question.id == uid_quest)
    result = session.scalar(
        query
    )
    if result:
        return result.answers.split(',')
    return None


# This function create and commit test into database
def create_test(
        session: Session,
        test: schemas.Test,
        questions: List[schemas.QuestionNew]
):
    """
        Create new test in database and pin all questions from test on it.
        :param session: sqlalchemy.orm.Session
        :param test: app.database.schemas.TestNew
        :param questions: list of app.database.schemas.QustionNew

    """
    test = models.Test(**test.model_dump())
    test.quests = [models.Question(**i.model_dump()) for i in questions]
    session.add(test)
    session.commit()


def delete_test(uid_test: int, session: Session):
    query = delete(models.Test).where(models.Test.id == uid_test)
    session.execute(query)
    session.commit()
