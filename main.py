import fastapi

from fastapi import FastAPI, Request, Path, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Annotated

from sqlalchemy.orm import Session

from app.app_database import database, crud, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="site_hiding.html", request=request
    )


@app.get("/tests")
async def list_of_tests(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    return templates.TemplateResponse(
        name="list_of_tests.html", context={"tests": crud.get_tests(db)}, request=request
    )


@app.get("/tests/{uid}")
async def test_page(uid: int, request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        name="page_of_test.html", context={"test": crud.get_test_by_id(uid, session=db)}, request=request
    )

