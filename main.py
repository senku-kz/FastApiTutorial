from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.get("/items")
async def get_item_list():
    return {"message": "item list"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users")
async def get_user_list():
    return {"message": "user list"}


@app.get("/users/me")
async def get_current_user():
    return {"user_id": "this is the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }

    return {"food_name": food_name, "message": "i like chocolate milk"}
