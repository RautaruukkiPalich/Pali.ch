import datetime
import json
import uvicorn
import logging

from fastapi import FastAPI, Response
from src.constants.const import HOST_URL
from src.app.funcs import create_short_url, check_short_url, check_long_url
from src.db.redisDB.redis_settings import start_redis
from starlette.responses import RedirectResponse


app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG,
    filename="..//../log/main_log.log",
)


@app.get("/")
async def index():
    return {"body": "main_page"}


@app.get("/{url}")
async def redirect_url(url: str):
    check, long_url = await check_short_url(short_url=url)
    if check:
        # return Response(
        #     content=json.dumps({"long_url": f"{long_url}"}),
        #     headers={'Content-type': 'application/json'},
        #     status_code=200,
        # )
        return RedirectResponse(
            url=long_url,
            headers={'Content-type': 'application/json'},
        )
    return Response(status_code=404)


@app.post("/create/")
async def post_long_url(long_url: str):
    check, short_url = await check_long_url(long_url=long_url)
    if not check:
        short_url = await create_short_url(long_url=long_url)
    content = json.dumps(
        {
            "long_url": long_url,
            "short_url": f"{HOST_URL}{short_url}",
        }
    )
    return Response(
        content=content,
        headers={'Content-type': 'application/json'},
        status_code=200,
    )


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
