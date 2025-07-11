from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from app.crud.hero import (
    create_hero,
    delete_hero,
    read_hero,
    read_heroes,
    update_hero,
)
from app.db.database import SessionDep
from app.schemas.hero import (
    HeroCreate,
    HeroPublic,
    HeroUpdate,
)
from app.utils.logger import get_logger

LOGGER_ROOT_NAME = f"::APP::API::ROUTES::{Path(__file__).stem}"
logger = get_logger(LOGGER_ROOT_NAME)

hero_router = APIRouter(prefix="/heroes", tags=["Heroes"])


@hero_router.post(
    "/",
    response_model=HeroPublic,
    status_code=status.HTTP_201_CREATED,
)
def add_new_hero(
    db_session: SessionDep,
    hero: HeroCreate,
):
    db_hero = create_hero(db_session, hero)
    return db_hero


@hero_router.get(
    "/",
    response_model=list[HeroPublic],
    status_code=status.HTTP_200_OK,
)
def list_all_heroes(
    db_session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    db_heroes = read_heroes(db_session, offset, limit)
    if len(db_heroes) == 0:
        msg = "Heroes not found"
        logger.debug(msg)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
    return db_heroes


@hero_router.get(
    "/{hero_id}",
    response_model=HeroPublic,
    status_code=status.HTTP_200_OK,
)
def get_hero_by_id(
    db_session: SessionDep,
    hero_id: int,
):
    db_hero = read_hero(db_session, hero_id)
    if not db_hero:
        msg = f"Hero with ID {hero_id} not found"
        logger.debug(msg)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
    return db_hero


@hero_router.patch(
    "/{hero_id}",
    response_model=HeroPublic,
    status_code=status.HTTP_202_ACCEPTED,
)
def update_existing_hero(
    db_session: SessionDep,
    hero_id: int,
    updated_hero: HeroUpdate,
):
    db_hero = update_hero(db_session, hero_id, updated_hero)
    if not db_hero:
        msg = f"Hero with ID {hero_id} not found"
        logger.debug(msg)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
    return db_hero


@hero_router.delete(
    "/{hero_id}",
    status_code=status.HTTP_202_ACCEPTED,
)
def delete_existing_hero(
    db_session: SessionDep,
    hero_id: int,
) -> dict:
    message = delete_hero(db_session, hero_id)
    if not message:
        msg = f"Hero with ID {hero_id} not found"
        logger.debug(msg)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg,
        )
    return message
