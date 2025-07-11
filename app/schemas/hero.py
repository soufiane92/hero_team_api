from sqlmodel import Field, Relationship, SQLModel

from app.schemas.team import Team


# Data model
class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")


# Table model
class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    team: Team | None = Relationship(back_populates="heroes")


# Public Data model
class HeroPublic(HeroBase):
    id: int


# Data model to create a Hero
class HeroCreate(HeroBase):
    secret_name: str


# Data model to update a Hero
class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None
