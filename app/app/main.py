import uvicorn
import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.db.redisDB.redis_settings import start_redis
from src.services import routers
from src.constants.const import ROOT
from src.services.exception_handlers import exception_handler_404
from datetime import datetime as dt

app = FastAPI()
app.include_router(routers.router)
app.mount('/static', StaticFiles(directory=f'{ROOT}/src/static/'), name='static')

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"{ROOT}/log/main_log.log",
)


@app.exception_handler(404)
async def handler_404(request, __):
    return await exception_handler_404(request)


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
