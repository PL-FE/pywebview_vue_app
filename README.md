# pywebview + FastApi+Vue+ElementUiPlus 

# 1.介绍  

**桌面应用开发，打包的环境整合**，**开发时**可使用node作为前端服务器，fastapi作为后端服务器（在pywebview启动时启动）。此时需要分别启动前后端的服务器。打包时只需启动pywebview即可（此时vue生成的dist会被挂在fastapi的服务器（uvicorn）上）



**项目目录：**

----pywebview_vue_app

├─dist 打包成exe的输出文件

├─gui vue打包后的静态文件
├─src
│  ├─backend  python代码
│  └─frontend vue项目所在文件





# 2.使用

## 2.1安装依赖



## （推荐）conda下使用

**conda下安装python,node ** 

```cmd
#安装python
conda create -n py38 python=3.8
# 激活python环境
conda activate py38
#在 Conda 环境中安装 Node.js
conda install -c conda-forge nodejs=v22.9.0
#
验证
python --version  # 检查 Python 版本
node -v           # 检查 Node.js 版本
npm -v            # 检查 npm 版本

```

**安装项目依赖**  

python的依赖

```cmd
pip install -r requirements.txt

```

node依赖

```
npm install --registry=http://registry.npmmirror.com  
```



# 3.启动

 main.py

```python
if __name__ == '__main__':
    find_port()
    uviconserverThread()
    fastServer("prod") # 值若为prod模拟打包后的启动，为dev则是开发环境启动。
```

**prod和dev的区别**

prod 此时启动项目后gui下的文件会被挂载到fastapi服务下，同时启动pywenview, 此时前端不用单独服务器了如（node）  

dev 此时启动项目仅仅启动fastapi和webview,前端需要使用npm run dev 单独启动。好处：方便前端页面开发  





# 4. 其他...







