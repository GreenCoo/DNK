import fastapi

from fastapi import FastAPI, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from sqlite3 import connect
from typing import Annotated

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


class Test(BaseModel):
    id: int
    name: str
    body: str
    answers: list[str]


some_tests = [Test(id=i, name=f"Some cool test number {i}", body=f"coolist body for test {i}", answers=["First", "Second"]) for i in range(10)]


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="site_hiding.html", request=request
    )

@app.get("/tests")
async def list_of_tests(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="list_of_tests.html", context={"tests": some_tests}, request=request
    )

@app.get("/tests/{uid}")
async def test_page(uid: int, request: Request):
    return templates.TemplateResponse(
        name="page_of_test.html", context=list(filter(lambda x: x.id == uid, some_tests))[0], request=request
    )
