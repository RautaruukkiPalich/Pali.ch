from fastapi import Request
from src.templates.index import get_templates
from src.constants.const import ROOT

templates = get_templates(f"{ROOT}/src/templates/html/")


async def exception_handler_404(request: Request):
    """
    :param request:
    :return: Template 404.html
    """
    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
        },
    )
