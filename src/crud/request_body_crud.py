from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

fake_items_db = []


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async  def create_item(item: Item):
    fake_items_db.append(item)
    return item

@app.get("/items")
async def read_item_list(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/itmes/{item_id}")
async def read_item(item_id: int):
    return fake_items_db[item_id-1]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    fake_items_db[item_id-1] = item
    return fake_items_db[item_id-1]


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    fake_items_db.remove(fake_items_db[item_id-1])

