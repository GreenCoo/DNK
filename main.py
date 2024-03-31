import fastapi
import uvicorn

from fastapi import FastAPI, Request, Path, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Annotated, Union, List

from sqlalchemy.orm import Session

from app.database import database, crud, models
from app.database.schemas import TestLight, Test, Question

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="./templates")


def get_db():
    session = database.SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    " This root of web app return index html "

    return templates.TemplateResponse(
        name="index.html",
        request=request
    )


@app.get("/tests")
async def list_of_tests(request: Request, session: Session = Depends(get_db)):
    " Return list of tests from database use crud functions "

    result = crud.get_tests(session)

    return templates.TemplateResponse(
        name="tests.html",
        context={"tests": result},
        request=request
    )


@app.get("/test/{tid}")
async def test_page(tid: int, request: Request, session: Session = Depends(get_db)):
    " Return main page of test with label and questions pages of this test "

    result = crud.get_test_by_id(tid, session)

    if result:
        return templates.TemplateResponse(
            name="test.html",
            context={"test": result},
            request=request
        )

    raise fastapi.HTTPException(status_code=404)


@app.get("/test/{uid}/{qid}")
async def test_page(uid: int, qid: int, request: Request, session: Session = Depends(get_db)):

    result = crud.get_question_by_id(uid, qid, session=session)

    if result is None:
        return RedirectResponse(url="/tests")

    return templates.TemplateResponse(
        name="question.html", context={"question": result},
        request=request
    )


# async def test_page(uid: int, qid: int, request: Request, session: Session = Depends(get_db)):
#     q = crud.get_question(qid, uid, session)
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
#

if __name__ == '__main__':
    uvicorn.run("main:app")

