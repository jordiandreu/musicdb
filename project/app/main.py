from fastapi import FastAPI

from app.db import init_db
from app.api.rest import router as rest_router
from app.api.gql import router as gql_router


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(
    rest_router,
#    prefix="/api",
#    tags=["api"],
    dependencies=[],
    responses={},
)

app.include_router(
    gql_router,
    prefix="/graphql")
