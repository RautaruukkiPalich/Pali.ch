import json
import re

from fastapi import APIRouter, Response, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from src.constants.const import HOST_URL
from src.app.funcs import create_short_url, check_short_url, check_long_url
from src.templates.index import get_templates
from src.constants.const import ROOT


router = APIRouter()
templates = get_templates(f"{ROOT}/src/templates/html/")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        },
    )


@router.get("/{url}", tags=["redirect"])
async def redirect_url(request: Request, url: str):
    check, long_url = await check_short_url(short_url=url)
    if check:
        return RedirectResponse(
            url=long_url,
            headers={'Content-type': 'application/json'},
        )
    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
        },
    )

    #return Response(status_code=404)


@router.post("/create/", tags=["shortly"])
async def post_long_url(data: dict = Body()):
    long_url = data["long_url"]
    regex = r"[-a-zA-Z0-9@:%_\+.~#?&\/=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&\/=]*)?"
    if not re.search(regex, long_url):
        content = json.dumps(
            {
                "error": "Invalid URL"
            }
        )
    else:
        check, short_url = await check_long_url(long_url=long_url)
        if not check:
            short_url = await create_short_url(long_url=long_url)
        content = json.dumps(
            {
                "error": None,
                "long_url": long_url,
                "short_url": f"{HOST_URL}{short_url}",
            }
        )
    return Response(
        content=content,
        headers={'Content-type': 'application/json'},
        status_code=200,
    )
