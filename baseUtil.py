''' -*- coding: utf-8 -*-
# @Author  : Ficus
# @Time    : 2024/11/5 15:34
# @File    : util.py
'''
import os
import sys
import subprocess

def get_root_path():
    '''
    获取项目根目录
    '''
    if hasattr(sys,'_MEIPASS'):
        return sys._MEIPASS

    return os.path.abspath(os.path.dirname(__file__))

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

    build("conda activate yolo8work")