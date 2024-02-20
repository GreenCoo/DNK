import sqlalchemy as sql

import sqlalchemy.orm as orm
from sqlalchemy import Table
from sqlalchemy import Engine, create_engine
from sqlalchemy import Column, Integer, String, MetaData

Base = orm.declarative_base()
engine = create_engine("sqlite:///../db/tests.db")


meta = MetaData()
TableOfQuestions = Table(
    'tests', meta,
    Column('id', Integer(), primary_key=True, index=True),
    Column('name', String(), nullable=False),
    Column('body', String(), nullable=False),
    Column('answers', String(), nullable=False)
)

# class TableOfQuestions(Base):
#     __tablename__ = "tests"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     body = Column(String)
#     answers = Column(String)


if __name__ == "__main__":
    with engine.connect() as conn:
        ins = TableOfQuestions.select()
        result = conn.execute(ins).fetchall()
        print(result[0])

