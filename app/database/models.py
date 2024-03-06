from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base
from typing import List, Union
from datetime import date


# TODO Make the datetime column and Make auto update with depend on time
class Test(Base):
    __tablename__ = "test"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    quests: Mapped[List['Question']] = relationship(back_populates="test", cascade="all,delete")

    # def __init__(self, id: Union[int, None], name: str):
    #     super().__init__()


class Question(Base):
    __tablename__ = "quest"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(nullable=False)
    type_answer: Mapped[int] = mapped_column(nullable=False)
    images: Mapped[str] = mapped_column(nullable=True)
    answers: Mapped[str] = mapped_column(nullable=False)
    test_id: Mapped[int] = mapped_column(ForeignKey(Test.id))

    test: Mapped[Test] = relationship(back_populates="quests")

    # def __init__(self, id: Union[int, None], body: str, type_answer: int, images: Union[str, None]):
    #     super().__init__()


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    # def __init__(self, id: Union[int, None], username: str, hashed_code: str):
    #     super().__init__()

