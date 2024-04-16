from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from .constants import URL_TO_DATABASE

engine = create_engine(url=URL_TO_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass

def recreate():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
