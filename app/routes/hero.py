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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero with ID {hero_id} not found",
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero with ID {hero_id} not found",
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero with ID {hero_id} not found",
        )
    return message
