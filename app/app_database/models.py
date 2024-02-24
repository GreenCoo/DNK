from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Test(Base):
    __tablename__ = "Test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    answers = Column(Text, nullable=False)
    users = relationship("TestUser", backref="test_id")


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    tests = relationship("TestUser", backref="user_id")


class TestUser(Base):
    __tablename__ = "TestUser"
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("Test.id"))
    user_id = Column(Integer, ForeignKey("User.id"))
