from pydantic import BaseModel
from typing import List


class TestBase(BaseModel):
    name: str
    body: str
    answers: list[str]


class Test(TestBase):
    id: int

    class Config:
        from_attributes = True


# TODO Make this class Users with base on class Users from Models.py
class Users(BaseModel):
    ...
