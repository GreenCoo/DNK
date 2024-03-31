from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from . import schemas
from typing import List, Union, Type
from datetime import date


# TODO Make the datetime column and Make auto update with depend on time
class Test(Base):

    __tablename__ = "test"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)

    questions: Mapped[List['Question']] = relationship(
        back_populates="test",
        cascade="all, delete",
        passive_deletes=True
    )

    def to_TestLight(self) -> schemas.TestLight:

        questions = len(self.questions)
        # questions = list(map(lambda x: x.id, self.questions))

        return schemas.TestLight(
            id=self.id,
            name=self.name,
            questions=questions
        )

    def to_Test(self) -> schemas.Test:

        questions = list(map(lambda x: x.to_Question(), self.questions))

        return schemas.Test(
            id=self.id,
            name=self.name,
            questions=questions
        )

    @classmethod
    def from_Test(cls, test: schemas.Test):

        questions = list(map(lambda x: Question.from_Question(x), test.questions))

        obj = cls(
            id=test.id,
            name=test.name,
            questions=questions
        )

        return obj

    # def __init__(self, id: Union[int, None], name: str):
    #     super().__init__()


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

    def to_Question(self) -> schemas.Question:
        images = self.images
        answers = self.answers.split(',')
        correct_answer = self.correct_answer.split(',')

        if images:
            images = images.split(',')

        dict_obj = self.__dict__
        dict_obj.update({"images": images, "answers": answers, "correct_answer": correct_answer})

        return schemas.Question(**dict_obj)

    @classmethod
    def from_Question(cls, question: schemas.Question):

        images = question.images
        answers = question.answers
        correct_answer = question.correct_answer

        if images:
            images = ",".join(images)

        answers = ",".join(answers)
        correct_answer = ",".join(correct_answer)

        question_dump = question.model_dump()
        question_dump.update({"answers": answers, "images": images, "correct_answer": correct_answer})

        obj = cls(**question_dump)

        return obj



class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    # def __init__(self, id: Union[int, None], username: str, hashed_code: str):
    #     super().__init__()

