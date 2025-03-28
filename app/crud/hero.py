from typing import Annotated
from fastapi import Query
from sqlmodel import select
from app.db.database import SessionDep
from app.schemas.hero import (
    Hero,
    HeroCreate,
    HeroPublic,
    HeroUpdate,
)


def create_hero(
    db_session: SessionDep,
    hero: HeroCreate,
) -> HeroPublic:
    db_hero = Hero.model_validate(hero)
    db_session.add(db_hero)
    db_session.commit()
    db_session.refresh(db_hero)
    return db_hero


def read_heroes(
    db_session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[HeroPublic]:
    db_heroes = db_session.exec(select(Hero).offset(offset).limit(limit)).all()
    return db_heroes


def read_hero(
    db_session: SessionDep,
    hero_id: int,
) -> HeroPublic:
    db_hero = db_session.get(Hero, hero_id)
    return db_hero


def update_hero(
    db_session: SessionDep,
    hero_id: int,
    updated_hero: HeroUpdate,
) -> HeroPublic:
    db_hero = db_session.get(Hero, hero_id)
    updated_hero_data = updated_hero.model_dump(exclude_unset=True)
    db_hero.sqlmodel_update(updated_hero_data)
    db_session.add(db_hero)
    db_session.commit()
    db_session.refresh(db_hero)
    return db_hero


def delete_hero(
    db_session: SessionDep,
    hero_id: int,
) -> dict:
    db_hero = db_session.get(Hero, hero_id)
    db_session.delete(db_hero)
    db_session.commit()
    return {"ok": f"Hero with ID {hero_id} deleted."}
