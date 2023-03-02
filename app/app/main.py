import uvicorn
import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.db.redisDB.redis_settings import start_redis
from src.services import routers
from datetime import datetime as dt


app = FastAPI()
app.include_router(routers.router)
app.mount('/static', StaticFiles(directory='../../src/static/'), name='static')

log_path = "../../log/"

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"{log_path}main_log.log",
)


@app.on_event("startup")
async def on_startup():
    logging.log(
        logging.INFO,
        f"{dt.now()}: server up...",
    )
    await start_redis()
    logging.log(
        logging.INFO,
        f"{dt.now()}: redis up...",
    )


@app.on_event("shutdown")
async def on_shutdown():
    logging.log(
        logging.INFO,
        f"{dt.now()}: server down... ",
    )


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        reload=True,
    )
