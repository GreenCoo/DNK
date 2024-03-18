import fastapi
import uvicorn

from fastapi import FastAPI, Request, Path, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
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
    session = database.SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        name="index.html",
        request=request
    )


@app.get("/tests")
async def list_of_tests(request: Request, session: Session = Depends(get_db)) -> HTMLResponse:
    result = crud.get_tests(session)
    print(result)
    return templates.TemplateResponse(
        name="tests.html",
        request=request
    )


@app.get("/get_tests")
async def get_tests(limit: int = None, session: Session = Depends(get_db)):
    if limit:
        return crud.get_tests(session, limit)
    return crud.get_tests(session)


@app.get("/tests/{uid}")
async def test_page(uid: int, request: Request, session: Session = Depends(get_db)):
    result = crud.get_test_by_id(uid, session)
    if result:
        return templates.TemplateResponse(
            name="page_of_test.html",
            context={"test": result},
            request=request
        )
    raise fastapi.HTTPException(status_code=404)


@app.get("/tests/{uid}/{qid}")
async def test_page(uid: int, qid: int, request: Request, session: Session = Depends(get_db)):
    result = crud.get_question_by_id(uid, qid, session=session)

    if result is None:
        return RedirectResponse(url="/tests")

    return templates.TemplateResponse(
        name="question_card.html", context={"question": result},
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

