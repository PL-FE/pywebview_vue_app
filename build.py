import os
import subprocess

def build_vue_project():
    print("Building Vue project...")
    frontend_dir = os.path.join(os.getcwd(), 'src', 'frontend')
    os.chdir(frontend_dir)
    # subprocess.run(['npm', 'run', 'build'], shell=True)
    os.chdir('../../')  # 返回根目录

def package_app():
    print("Packaging app...")
    main_spec = os.path.join(os.getcwd(), 'main.spec')
    subprocess.run(['pyinstaller','-y', main_spec], shell=True)
    # 打开当前文件夹
    subprocess.run(['start', 'dist'], shell=True)

def main():
    build_vue_project()
    package_app()

if __name__ == "__main__":
    main()
