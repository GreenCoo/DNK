from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from . import schemas
from typing import Any, List, Union, Type
from datetime import date
from fastapi.encoders import jsonable_encoder


# TODO Make the datetime column and Make auto update with depend on time
class Test(Base):

    def __init__(self, **kw: Any):
        super().__init__(**kw)

    __tablename__ = "test"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    questions: Mapped[List['Question']] = relationship(
        back_populates="test",
        cascade="all, delete",
        passive_deletes=True
    )


class Question(Base):
    __tablename__ = "quest"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()
    images: Mapped[str] = mapped_column(nullable=True)

    type_answer: Mapped[int] = mapped_column()
    answers: Mapped[str] = mapped_column()
    correct_answer: Mapped[str] = mapped_column()

    test_id: Mapped[int] = mapped_column(ForeignKey(Test.id, ondelete="CASCADE"))
    test: Mapped[Test] = relationship(back_populates="questions")


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)


