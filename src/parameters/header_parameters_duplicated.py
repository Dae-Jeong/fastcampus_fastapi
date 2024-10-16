from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_item(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
