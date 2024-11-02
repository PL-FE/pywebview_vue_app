import logging
from contextlib import redirect_stdout
from io import StringIO
from threading import Thread

import uvicorn
import webview

from fastapp.app import app as fastApp

logger = logging.getLogger(__name__)



def uviconserver():
    uvicorn.run(fastApp, host="localhost", port=8000)

def uviconserverThread():
    uvth=Thread(target=uviconserver)
    uvth.setDaemon(True)
    uvth.start()

def fastServer():
    print()
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('flask pywebview application', "http://localhost:3000")
        webview.start(func=uviconserverThread,debug=True)

def flaskServer():
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('fastapi pywebview application', "http://localhost:3000")
        webview.start(debug=True)

if __name__ == '__main__':
    # 运行flask
    # flaskServer()
#     运行fastapi
    fastServer()

