from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.app_database import crud, models, schemas
from app.app_database.database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    print(
        crud.get_tests(SessionLocal)
    )