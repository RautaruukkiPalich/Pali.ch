import datetime
import uvicorn
import logging

from fastapi import FastAPI
from src.db.redisDB.redis_settings import start_redis
from src.services import routers


app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG,
    filename="..//../log/main_log.log",
)


@app.get("/")
async def index():
    return {"body": "main_page"}


app.include_router(routers.router)


@app.on_event("startup")
async def on_startup():
    logging.log(logging.INFO, f"{datetime.datetime.now()}: server up...")
    await start_redis()
    logging.log(logging.INFO, f"{datetime.datetime.now()}: redis up...")


@app.on_event("shutdown")
async def on_shutdown():
    logging.log(logging.INFO, f"{datetime.datetime.now()}: server down... ")


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        reload=True,
    )
