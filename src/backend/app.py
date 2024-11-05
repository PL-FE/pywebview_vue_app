''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/2 09:36
# @File    : fastServer.py
'''
import os
from typing import Dict, Any

from pydantic import BaseModel
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from router import routerTest
import  baseUtil


# 前端文件目录
dist_dir = os.path.join(baseUtil.get_root_path(), "gui")
print(f'dist_dir:{dist_dir}')

app = FastAPI(docs_url=None)
# 注册路由
app.include_router(routerTest.router)
app.mount("/static",StaticFiles(directory=dist_dir),name="static")
class BaseMap(BaseModel):
    data: Dict[str, Any]
