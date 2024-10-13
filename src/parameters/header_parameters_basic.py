from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_item(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
