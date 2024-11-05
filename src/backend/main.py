import random
from contextlib import redirect_stdout
from io import StringIO
from threading import Thread

import uvicorn
import webview
from loguru import logger
from app import app as fastApp
import baseUtil





def find_port():
    global port
    while True:
        try:
            port=baseUtil.find_port(port)
            logger.info(f" Uviconserver  port:{port}")
            break
        except Exception as e:
            logger.error(f"Exception Uviconserver error repeat port:{port}")
            port = random.randint(18000, 20000)
def uviconserver():
    global port
    uvicorn.run(fastApp, host="localhost", port=port)


def uviconserverThread():
    uvth=Thread(target=uviconserver)
    uvth.setDaemon(True)
    uvth.start()



def fastServer(envMode):
    """
    根据模式启动
    @param envMode:  dev，开发环境，prod，打包环境
    @return:
    """
    stream = StringIO()
    with redirect_stdout(stream):
        if envMode=="dev":
            # "http://localhost:3000" 前端node启动时的端口号，在vite.config.js 中配置
            window = webview.create_window('flask pywebview application', "http://localhost:3000")
        else:
            window = webview.create_window('flask pywebview application', "http://localhost:"+str(port) )
        webview.start(debug=True)

#默认端口号，如果重复则随机选取一个
port =8000

if __name__ == '__main__':
    find_port()
    uviconserverThread()
    fastServer("prod")
