import json

from fastapi import APIRouter, Response
from starlette.responses import RedirectResponse
from src.constants.const import HOST_URL
from src.app.funcs import create_short_url, check_short_url, check_long_url

router = APIRouter()


@router.get("/{url}", tags=["redirect"])
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


@router.post("/create/", tags=["shortly"])
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
