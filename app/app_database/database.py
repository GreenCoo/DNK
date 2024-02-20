from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

URL_TO_DATABASE = "sqlite:///./app/app_database/tests.db"

engine = create_engine(url=URL_TO_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)
Base = declarative_base()
