from fastapi import FastAPI, Request
from typing import Any
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")

NAME_HTML: str = "test.html"
CONTEXT: dict[str: Any] = {"test": "test2"}


@app.get("/")
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, context=CONTEXT, name=NAME_HTML)
