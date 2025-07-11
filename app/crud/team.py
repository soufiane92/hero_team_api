from typing import Annotated

from fastapi import Query
from sqlmodel import select

from app.db.database import SessionDep
from app.schemas.team import (
    Team,
    TeamCreate,
    TeamPublic,
    TeamUpdate,
)


def create_team(
    db_session: SessionDep,
    team: TeamCreate,
) -> TeamPublic:
    db_team = Team.model_validate(team)
    db_session.add(db_team)
    db_session.commit()
    db_session.refresh(db_team)
    return db_team


def read_teams(
    db_session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[TeamPublic]:
    db_teams = db_session.exec(select(Team).offset(offset).limit(limit)).all()
    return db_teams


def read_team(
    db_session: SessionDep,
    team_id: int,
) -> TeamPublic:
    db_team = db_session.get(Team, team_id)
    return db_team


def update_team(
    db_session: SessionDep,
    team_id: int,
    updated_team: TeamUpdate,
) -> TeamPublic:
    db_team = db_session.get(Team, team_id)
    updated_team_data = updated_team.model_dump(exclude_unset=True)
    db_team.sqlmodel_update(updated_team_data)
    db_session.add(db_team)
    db_session.commit()
    db_session.refresh(db_team)
    return db_team


def delete_team(
    db_session: SessionDep,
    team_id: int,
) -> dict:
    db_team = db_session.get(Team, team_id)
    db_session.delete(db_team)
    db_session.commit()
    return {"ok": f"Team with ID {team_id} deleted."}
