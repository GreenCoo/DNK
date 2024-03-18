from pydantic import BaseModel
from typing import List, Union, Optional


class Question(BaseModel):
    id: Optional[int] = None
    name: str
    body: str
    type_answer: int
    images: Optional[List[str]] = None
    answers: List[str]
    correct_answer: List[str]


class Test(BaseModel):
    id: Optional[int] = None
    name: str
    questions: List[Question]


class TestLight(Test):
    questions: int  # count of tests


# TODO Make this class Users with base on class Users from Models.py
class Users(BaseModel):
    ...
