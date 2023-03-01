import random

from src.constants.const import SYMBOLS, POPULAR_URLS
from src.db import funcs as db


async def generate_short_url(length: int):
    short_url = ''.join([random.choice(SYMBOLS) for _ in range(length)])
    return short_url


async def create_short_url(long_url: str):
    length = 7 if any([url in long_url for url in POPULAR_URLS]) else 6
    while True:
        short_url = await generate_short_url(length)
        check, _ = await check_short_url(short_url=short_url)
        if not check:
            await save_urls(
                long_url=long_url,
                short_url=short_url,
            )
            break
    return short_url


async def check_short_url(short_url: str):
    check, urls = await db.check_url(
        type_url="short_url",
        url=short_url,
    )
    if not check:
        return check, None
    return check, urls["long_url"]


async def check_long_url(long_url: str):
    check, urls = await db.check_url(
        type_url="long_url",
        url=long_url,
    )
    if not check:
        return check, None
    return check, urls["short_url"]


async def save_urls(long_url: str, short_url: str):
    await db.save_urls(
        long_url=long_url,
        short_url=short_url,
    )
