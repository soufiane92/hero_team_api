from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from app.utils.logger import get_logger

LOGGER_ROOT_NAME = f"::APP::DB::{Path(__file__).stem}"
logger = get_logger(LOGGER_ROOT_NAME)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    try:
        logger.info("Creating tables...")

        SQLModel.metadata.create_all(engine)
        logger.info("Tables created successfully.")
    except Exception as e:
        logger.exception(f"Error initializing database: {e}")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
