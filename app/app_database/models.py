from sqlalchemy import Column, Integer, String, Text, Boolean
from .database import Base


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    answers = Column(Text, nullable=False)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    id_in_test = Column(Integer, nullable=False)
    test_id = Column(Integer, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    is_choosing = Column(Boolean, nullable=False)
    answer_options = Column(String)



# TODO make this user class with relationship from Test
# class User(Base):
#     ...

