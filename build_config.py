import PyInstaller.__main__
import os
import sys

# 确保图标文件存在
if not os.path.exists('pdf_reverser.png'):
    # 如果没有图标文件，先运行生成图标的脚本
    exec(open('pdf_icon.py').read())

# 获取customtkinter包的路径
import customtkinter
ctk_path = os.path.dirname(customtkinter.__file__)

# 根据操作系统设置路径分隔符
if sys.platform == "win32":
    separator = ";"
else:
    separator = ":"

# PyInstaller打包配置
PyInstaller.__main__.run([
    'reverse_pdf_gui.py',
    '--name=PDF页面顺序反转工具',
    '--windowed',
    '--icon=pdf_reverser.png',
    f'--add-data=pdf_reverser.png{separator}.',
    f'--add-data={ctk_path}{separator}customtkinter',
    '--onefile',
    '--clean',
    '--noconfirm',
    '--hidden-import=customtkinter',
    '--hidden-import=tkinter',
    '--hidden-import=PIL',
    '--hidden-import=PIL._tkinter_finder',
    '--collect-all=customtkinter',
    '--uac-admin',
    '--disable-windowed-traceback',
    '--runtime-hook=runtime_hook.py'
]) 