from fastapi import FastAPI
from app.db.database import create_db_and_tables
from app.routes.hero import hero_router
from app.routes.team import team_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(hero_router)
app.include_router(team_router)
