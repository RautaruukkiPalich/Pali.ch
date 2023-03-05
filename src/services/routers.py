import json
import re


from fastapi import APIRouter, Response, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from src.app.funcs import create_short_url, check_short_url, check_long_url
from src.templates.index import get_templates
from src.constants.const import HOST_URL, ROOT
from src.services.exception_handlers import exception_handler_404


router = APIRouter()
templates = get_templates(f"{ROOT}src/templates/html/")


@router.get("/", response_class=HTMLResponse, tags=["index"])
async def index(request: Request):
    """
    :param request: Request
    """
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        },
    )


@router.get("/{url}", tags=["get-long-url"])
async def redirect_url(request: Request, url):
    """
    :param request: Request
    :param url: str
    """
    url = str(url)
    check, long_url = await check_short_url(short_url=url)
    if check:
        return RedirectResponse(
            url=long_url,
            headers={'Content-type': 'application/json'},
        )
    return await exception_handler_404(request)


@router.post("/create/", tags=["create-short-url"])
async def post_long_url(data: dict = Body()):
    """
    :param data: {'long_url': str}
    """
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
