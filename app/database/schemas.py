from pydantic import BaseModel
from typing import List, Union


class QuestionBase(BaseModel):
    id: int
    body: str
    type_answer: int
    images: Union[str, None] = None
    answers: str


class QuestionNew(QuestionBase):
    id: Union[int, None] = None


class TestBase(BaseModel):
    id: int
    name: str


class TestNew(TestBase):
    id: Union[int, None] = None


class Test(TestBase):
    # answers: List[QuestionBase]

    class Config:
        from_attributes = True


# TODO Make this class Users with base on class Users from Models.py
class Users(BaseModel):
    ...
