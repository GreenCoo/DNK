import fastapi as api

app = api.FastAPI()

@app.get("/users/me")
async def me():
    return

@app.get("/users/{user_id}")
async def users(id: int):
    return id

