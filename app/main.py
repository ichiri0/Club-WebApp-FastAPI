import logging
from fastapi import FastAPI

from db import init_db
from api import api_router
from fastapi.middleware.cors import CORSMiddleware

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    return application


app = create_application()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники, или укажите конкретные
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы, или укажите конкретные
    allow_headers=["*"],  # Разрешить все заголовки, или укажите конкретные
)

# @app.on_event("startup")
# async def startup_event():
#     print("Connecting to database...")
#     await Tortoise.init(
#         db_url=os.environ.get("DATABASE_URL"),
#         modules={"models": ["app.database.models.user"]}
#     )
#     await Tortoise.generate_schemas()

# @app.on_event("shutdown")
# async def shutdown_event():
#     await Tortoise.close_connections()


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
