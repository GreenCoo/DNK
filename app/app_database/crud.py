from . import schemas, models
from .database import SessionLocal

from sqlalchemy.orm import Session


def get_tests(session: Session, limit: int | None = None):
    if limit:
        return session.query(models.Test).limit(limit).all()
    return session.query(models.Test).all()


def get_test_by_id(uid: int, session: Session):
    return session.query(models.Test).filter(models.Test.id == uid).first()