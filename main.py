import fastapi

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = fastapi.FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


@app.get("/{name}")
async def root(request: Request, name: str) -> HTMLResponse:
    return templates.TemplateResponse(
        name="index.html", context={"name": name}, request=request
    )
