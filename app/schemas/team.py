from sqlmodel import SQLModel, Field, Relationship


# Data model
class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


# Table model
class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    heroes: list["Hero"] = Relationship(back_populates="team")


# Public Data model
class TeamCreate(TeamBase):
    pass


# Data model to create a Team
class TeamPublic(TeamBase):
    id: int


# Data model to update a Team
class TeamUpdate(TeamBase):
    name: str | None = None
    headquarters: str | None = None
