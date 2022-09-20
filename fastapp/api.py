from fastapi import FastAPI, Depends, Request
from starlette.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.http import HTTPBearer
import time

app = FastAPI(title="FastAPI on Azure")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
bearer = HTTPBearer(scheme_name="bearer")

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/auth/", dependencies=[Depends(bearer)])
async def auth_items():
    return {"token": "token"}


if __name__ == '__main__':
    app.run