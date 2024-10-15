from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/headers/")
def get_headers():
    headers = {"Content-Type": "application/json"}
    content = {"message": "Hello World"}
    return JSONResponse(content=content, headers=headers)
