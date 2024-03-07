from pydantic import BaseModel
from typing import List, Union, Optional


class Question(BaseModel):
    id: Optional[int] = None
    body: str
    type_answer: int
    images: Optional[List[str]] = None
    answers: List[str]


# class NewQuestionInDB(Question):
#     id: Optional[int] = None
#     answers: str


class Test(BaseModel):
    id: Optional[int] = None
    name: str
    questions: List[Question]


class TestLight(Test):
    questions: List[int]


# class NewTestInDB(Test):
#     id: Optional[int] = None
#     questions: List[NewQuestionInDB]


# class Test(TestBase):
#
#     class Config:
#         from_attributes = True


# TODO Make this class Users with base on class Users from Models.py
class Users(BaseModel):
    ...
