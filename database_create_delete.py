from app.database import database, crud, schemas, models
from icecream import ic

questions = [
    schemas.Question(
        body=f"CoolBody{i}",
        name=f"CoolName{i}",

        type_answer=1,
        answers=['1', '3', '3'],
        correct_answer=['3']
    )
    for i in range(3)
]

test = schemas.Test(
    id=999,
    name="CoolName2",
    questions=questions
)


with database.SessionLocal() as Session:
    ic(crud.create_test(test, Session))
    ic(crud.delete_test(test.id, Session))
