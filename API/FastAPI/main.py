"""
Description:
Author:qxy
Date: 2019/12/2 7:32 下午
File: FastAPI 
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"Hello": "World"}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


