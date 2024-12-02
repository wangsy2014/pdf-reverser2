#!/bin/bash

# 安装必要的依赖
pip install auto-py-to-exe customtkinter PyPDF2 pillow

# 生成图标
python pdf_icon.py

# 启动图形界面打包工具
auto-py-to-exe

# 或者使用命令行方式打包
# auto-py-to-exe --config auto_py_config.json

echo "请在打开的图形界面中："
echo "1. 选择 'reverse_pdf_gui.py' 作为脚本文件"
echo "2. 选择 'ONE FILE' 模式"
echo "3. 选择 'WINDOW BASED' 模式"
echo "4. 在 'Icon' 中选择 'pdf_reverser.png'"
echo "5. 在 'Additional Files' 中添加 pdf_reverser.png"
echo "6. 在 'Advanced' 中添加以下 hidden imports:"
echo "   - customtkinter"
echo "   - tkinter"
echo "   - PIL"
echo "   - PIL._tkinter_finder"
echo "7. 点击 'CONVERT .PY TO .EXE'" 