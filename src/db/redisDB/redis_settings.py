import aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache


async def start_redis():
    pass
#    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
#    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
#
#redis_cache = cache()
