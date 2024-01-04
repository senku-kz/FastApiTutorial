from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def read_items(
    required_query: str = Query(...),
    query_list: list[str] | None = Query(None),
    query_list2: list[str] = Query(["foo", "bar"]),
    q: str | None = Query(
        None,
        min_length=3,
        max_length=10,
        title="Sample query string",
        description="This is a sample query string.",
        # alias="item-query",
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"required_query": required_query})
        results.update({"query_list": query_list})
        results.update({"query_list2": query_list2})
        results.update({"q": q})
    return results


@app.get("/items_hidden")
async def hidden_query_route(
    hidden_query: str | None = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}
