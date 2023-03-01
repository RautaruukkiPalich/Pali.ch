import json
import random
import uvicorn
import logging

from fastapi import FastAPI, Response
from src.app.constants import HOST_URL, SYMBOLS
from starlette.responses import RedirectResponse

app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG,
    filename="main_log.log",
)

long_to_short = {}  # TODO use DB
short_to_long = {}  # TODO use DB


async def get_short_url_from_db(long_url: str):
    short = long_to_short.get(long_url, "")
    return short


async def get_long_url_from_db():
    pass


async def save_urls_in_db(long_url: str, short_url: str):
    # TODO book short url
    # TODO add to Redis
    long_to_short[long_url] = short_url
    short_to_long[short_url] = long_url


async def get_short_url():
    short_url = ''.join([random.choice(SYMBOLS) for _ in range(6)])
    return short_url


async def get_available_short_url():
    while True:
        short_url = await get_short_url()
        if short_url not in long_to_short:
            break
    return short_url


@app.get("/")
async def index():
    return {"body": "main_page"}


@app.get("/{url}")
async def redirect_url(url: str):
    if url in short_to_long:
        return Response(
            content=json.dumps({"long_url": f"{short_to_long[url]}"}),
            headers={'Content-type': 'application/json'},
        )
        # TODO use RedirectResponse
        # return RedirectResponse(
        #     url=short_to_long[url],
        #     headers={'Content-type': 'application/json'},
        # )
    return Response(status_code=404)


@app.post("/create/")
async def post_long_url(long: str):
    short = await get_short_url_from_db(long_url=long)
    if not short:
        valid_url = await get_available_short_url()
        short = f"{valid_url}"
        await save_urls_in_db(
            long_url=long,
            short_url=short,
        )
    content = json.dumps(
        {
            "long": long,
            "short": f"{HOST_URL}{short}",
        }
    )
    return Response(
        content=content,
        status_code=200,
    )


if __name__ == "__main__":
    print('started')
    uvicorn.run(
        "__main__:app",
        reload=True,
    )
