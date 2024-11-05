''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/5 15:34
# @File    : util.py
'''
import os
import sys
import subprocess
import socketserver
def get_root_path():
    '''
    获取项目根目录
    '''
    if hasattr(sys,'_MEIPASS'):
        return sys._MEIPASS

    return os.path.abspath(os.path.dirname(__file__))


def find_port(port=None):
    port = 0 if port is None else port
    with socketserver.TCPServer(("localhost",port),None) as server:
        return server.server_address[1]


def build(cmd=""):
    '''
    打包成exe
    '''
    # 激活conda环境 没有则不用

    result=subprocess.run(cmd+ " && pyinstaller main.spec",shell=True,capture_output=True,text=True)
    print(result)



if __name__ == '__main__':
    root_path=get_root_path()
    print("root_path",root_path)
    print(f'findport:{find_port(8000)}')
    build("conda activate yolo8work")
