import fastapi as api


app = api.FastAPI()


@app.get("/")
async def root():
    return
