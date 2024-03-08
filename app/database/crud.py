from . import schemas, models
from sqlalchemy import select, Row, delete
from sqlalchemy.orm import Session
from typing import Union, List, Sequence, Optional

"""
    Этот файл нужен для работы с базой данных и преобразования ответов моделей в pydantic модели. Валидация и защита от 
    sql injections делается в main ...
"""


# TODO remake this function with get only id and name from database
def get_tests(session: Session, limit: int = 10) -> List[schemas.TestLight]:
    query = select(models.Test)

    if limit:
        query = query.limit(limit)

    tests = session.scalars(query).all()

    return list(map(lambda x: x.to_TestLight(), tests))


def get_test_by_id(uid_test: int, session: Session) -> Optional[models.Test]:
    result = session.get(models.Test, uid_test)

    return result


def get_question_by_id(uid_test: int, uid_quest: int, session: Session) -> Optional[models.Question]:
    """
    :param uid_test: id of test
    :param uid_quest: id of question pin on test
    :param session: session for work with orm models from sqlalchemy
    :return: models.Question
    """

    query = select(models.Question) \
        .where(models.Question.test_id == uid_test, models.Question.id == uid_quest)

    result = session.scalar(
        query
    )

    return result


# This function create and commit test into database
def create_test(
        test_new: schemas.Test,
        session: Session
):
    """
        Create new test in database and pin all questions from test on it.
        :param session: sqlalchemy.orm.SessionInDB
        :param test_new: app.database.schemas.Test
    """
    test = models.Test.from_Test(test_new)
    session.add(test)
    session.commit()


def delete_test(uid_test: int, session: Session):
    test = get_test_by_id(uid_test, session)
    list(map(lambda x: session.delete(x), test.questions))
    session.delete(test)
    session.commit()

