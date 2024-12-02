#!/bin/bash

# 设置 Wine 环境
export WINEARCH=win64
export WINEPREFIX=~/.wine

# 创建输出目录
mkdir -p dist

# 安装 Python 依赖（如果还没安装）
pip install pyinstaller customtkinter PyPDF2 pillow

# 修改 PyInstaller 配置以适应 Windows 目标
cat > wine_build_config.py << EOL
import PyInstaller.__main__
import os
import sys

# 获取customtkinter包的路径
import customtkinter
ctk_path = os.path.dirname(customtkinter.__file__)

# Windows 路径分隔符
separator = ";"

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
    '--target-architecture=x86_64',
    '--target-platform=win32',
])
EOL

# 生成图标
python pdf_icon.py

# 使用 Wine 和 PyInstaller 打包
wine python -m PyInstaller wine_build_config.py

echo "打包完成！可执行文件位于 dist/PDF页面顺序反转工具.exe" 