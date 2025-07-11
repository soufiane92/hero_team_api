from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from app.crud.team import (
    create_team,
    delete_team,
    read_team,
    read_teams,
    update_team,
)
from app.db.database import SessionDep
from app.schemas.team import (
    TeamCreate,
    TeamPublic,
    TeamUpdate,
)

team_router = APIRouter(prefix="/teams", tags=["Teams"])


@team_router.post(
    "/",
    response_model=TeamPublic,
    status_code=status.HTTP_201_CREATED,
)
def add_new_team(
    db_session: SessionDep,
    team: TeamCreate,
):
    db_team = create_team(db_session, team)
    return db_team


@team_router.get(
    "/",
    response_model=list[TeamPublic],
    status_code=status.HTTP_200_OK,
)
def list_all_teams(
    db_session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    db_teams = read_teams(db_session, offset, limit)
    return db_teams


@team_router.get(
    "/{team_id}",
    response_model=TeamPublic,
    status_code=status.HTTP_200_OK,
)
def get_team_by_id(
    db_session: SessionDep,
    team_id: int,
):
    db_team = read_team(db_session, team_id)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
    return db_team


@team_router.patch(
    "/{team_id}",
    response_model=TeamPublic,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_existing_team(
    db_session: SessionDep,
    team_id: int,
    updated_team: TeamUpdate,
):
    db_team = update_team(db_session, team_id, updated_team)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
    return db_team


@team_router.delete(
    "/{team_id}",
    status_code=status.HTTP_202_ACCEPTED,
)
def delete_existing_team(
    db_session: SessionDep,
    team_id: int,
) -> dict:
    message = delete_team(db_session, team_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
    return message
