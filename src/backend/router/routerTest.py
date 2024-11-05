''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/4 15:14
# @File    : server.py
'''
import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from loguru import logger

import baseUtil
router = APIRouter()
dist_dir = os.path.join(baseUtil.get_root_path(), "gui")

@router.get("/",response_class=HTMLResponse)
def hello():
    indexpath = os.path.join(dist_dir,"index.html")
    with open(indexpath) as f:
        return f.read()


@router.post("/test")
def test(data: dict):
    logger.info(f'test:{data}')
    return {"message": "This is a test"}
