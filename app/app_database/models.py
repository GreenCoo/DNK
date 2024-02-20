from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    answers = Column(Text, nullable=False)


# TODO make this user class with relationship from Test
# class User(Base):
#     ...

