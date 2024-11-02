''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/2 09:36
# @File    : fastServer.py
'''


from fastapi import FastAPI
app = FastAPI(docs_url=None)


@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}