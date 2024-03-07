import fastapi

from fastapi import FastAPI, Request, Path, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Annotated

from sqlalchemy.orm import Session

from app.database import database, crud, models

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
    pass


# @app.get("/tests/{uid}/{qid}")
# async def test_page(uid: int, qid: int, request: Request, db: Session = Depends(get_db)):
#     q = crud.get_question(qid, uid, db)
#     if q is None:
#         return RedirectResponse(url="/tests")
#
#     if not q.answer_options is None:
#         options = q.answer_options.split(';')
#     else:
#         options = []
#     return templates.TemplateResponse(
#         name="question_card.html", context={"q": q,
#         "options": options}, request=request
#     )
#

