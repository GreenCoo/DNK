import fastapi

from fastapi import FastAPI, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Annotated

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="index.html", context={"tests": [1, 2, 3, 4, 5]}, request=request
    )

@app.get("/{test}")
async def page_of_test(request: Request,
                       test: Annotated[str, Path(regex=r'^[a-zA-Z0-9\_] \* $')]
                       ) -> HTMLResponse:
    return
