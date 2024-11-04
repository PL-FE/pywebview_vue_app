''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/2 09:36
# @File    : fastServer.py
'''
from typing import Dict, Any

from pydantic import BaseModel
from fastapi import FastAPI
from loguru import logger

app = FastAPI(docs_url=None)


class BaseMap(BaseModel):
    data: Dict[str, Any]


@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.post("/test")
def test(data: dict):
    logger.info(f'test:{data}')
    return {"message": "This is a test"}
