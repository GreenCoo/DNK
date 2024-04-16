from . import schemas, models
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional, Any, Union

"""
    Этот файл нужен для работы с базой данных и преобразования ответов моделей в pydantic модели.
    Валидация и защита от sql injections делается в main ...
"""

# Функции для чтение из базы данных.

def get_tests(session: Session, limit: int = 10) -> List[models.Test]:
    
    query = select(models.Test)

    if limit:
        query = query.limit(limit)

    tests = session.scalars(query).all()

    return list(tests)


def get_test(uid_test: int, session: Session) -> Optional[models.Test]:

    test = session.get(models.Test, uid_test)

    return test

# Функции для конвертирования данных.



# Функции для изменения базы данных.

