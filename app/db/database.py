from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    try:
        print("Creating tables...")
        from app.schemas.hero import Hero
        from app.schemas.team import Team

        SQLModel.metadata.create_all(engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
