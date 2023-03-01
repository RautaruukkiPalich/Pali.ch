from src.db.mongoDB.mongo_settings import series_collection


async def insert_document(collection, data):
    return collection.insert_one(data).inserted_id


async def get_document(collection, type_url: str, url: str):
    data = {type_url: url}
    return collection.find_one(data)


async def check_url(type_url: str, url: str):
    res = await get_document(series_collection, type_url, url)
    if not res:
        return False, res
    return True, res


async def save_urls(long_url: str, short_url: str):
    data = {
        "long_url": long_url,
        "short_url": short_url,
    }
    await insert_document(series_collection, data)
