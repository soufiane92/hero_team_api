from typing import Any
from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.routes.hero import add_new_hero
from app.schemas.hero import Hero

import pytest


def test_list_all_heroes(
    client: TestClient,
    session: Session,
) -> None:
    new_test_hero_1 = add_new_hero(
        session,
        Hero(name="test_name_1", secret_name="test_secret_1"),
    )
    new_test_hero_2 = add_new_hero(
        session,
        Hero(name="test_name_2", secret_name="test_secret_2", age=45),
    )
    response = client.get("/heroes/")
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(data) == 2

    for i, new_test_hero in zip(
        range(len(data)),
        [new_test_hero_1, new_test_hero_2],
    ):
        assert data[i]["name"] == new_test_hero.name
        assert data[i]["team_id"] == new_test_hero.team_id
        assert data[i]["age"] == new_test_hero.age
        assert data[i]["id"] == new_test_hero.id


def test_get_hero_by_id(
    session: Session,
    client: TestClient,
) -> None:
    new_test_hero = add_new_hero(
        session,
        Hero(name="test_name", secret_name="test_secret"),
    )
    response = client.get(f"/heroes/{new_test_hero.id}")

    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data["name"] == new_test_hero.name
    assert data["team_id"] == new_test_hero.team_id
    assert data["age"] == new_test_hero.age
    assert data["id"] == new_test_hero.id


@pytest.mark.parametrize(
    "json_data, response_status_code",
    [
        (
            {"name": "test_name", "secret_name": "test_secret"},
            status.HTTP_201_CREATED,
        ),
        (
            {"name": "test_name"},
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ),
        (
            {
                "name": "test_name",
                "secret_name": {"message": "test_secret"},
            },
            status.HTTP_422_UNPROCESSABLE_ENTITY,
        ),
    ],
)
def test_add_new_hero(
    client: TestClient,
    json_data: dict,
    response_status_code: Any,
) -> None:
    response = client.post(
        "/heroes/",
        json=json_data,
    )

    assert response.status_code == response_status_code

    if response.status_code == status.HTTP_201_CREATED:
        data = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        assert data["name"] == "test_name"
        assert data["team_id"] is None
        assert data["age"] is None
        assert data["id"] is not None
    else:
        assert "detail" in response.json()
