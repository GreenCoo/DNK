import sqlalchemy as sql

import sqlalchemy.orm as orm
from sqlalchemy import Table
from sqlalchemy import Engine, create_engine
from sqlalchemy import Column, Integer, String, MetaData

Base = orm.declarative_base()
engine = create_engine("sqlite:///../db/tests.db")


if __name__ == "__main__":
    print(0)
