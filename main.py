import fastapi
import uvicorn

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

from typing import Annotated, Optional, Union, List

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

    result = crud.get_test(tid, session)

    if result:
        result = jsonable_encoder(result)
        
        return templates.TemplateResponse(
            name="test.html",
            context={"test": result},
            request=request
        )
    
    raise fastapi.HTTPException(status_code=404)


@app.get("/test/questions/{id}")
def questions(id: int, session: Session = Depends(get_db)):

    result = crud.get_test(id, session=session)
    
    if result:
        return jsonable_encoder(result.questions, exclude={"correct_answer"})
    
    raise fastapi.HTTPException(status_code=404)

if __name__ == '__main__':
    uvicorn.run("main:app")

