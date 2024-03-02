from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from typing import List


class Test(Base):
    __tablename__ = "test"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    quests: Mapped[List['Question']] = relationship(back_populates="test")


class Question(Base):
    __tablename__ = "quest"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(nullable=True)
    type_answer: Mapped[int] = mapped_column(nullable=False)
    images: Mapped[str]
    answers: Mapped[str] = mapped_column(nullable=False)
    test_id: Mapped[int] = mapped_column(ForeignKey(Test.id))

    test: Mapped[Test] = relationship(back_populates="quests")


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_code: Mapped[str] = mapped_column(nullable=False)


