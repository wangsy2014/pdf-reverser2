import PyInstaller.__main__
import os
import sys

def main():
    # 生成图标
    import pdf_icon
    if not pdf_icon.create_icon():
        print("Error: Failed to create icon")
        sys.exit(1)

    # 获取customtkinter包的路径
    import customtkinter
    ctk_path = os.path.dirname(customtkinter.__file__)

    # PyInstaller配置
    PyInstaller.__main__.run([
        'reverse_pdf_gui.py',
        '--name=PDF页面顺序反转工具',
        '--windowed',
        '--onefile',
        '--icon=pdf_reverser.png',
        '--add-data=pdf_reverser.png;.',
        '--add-data=%s;customtkinter' % ctk_path,
        '--hidden-import=customtkinter',
        '--hidden-import=tkinter',
        '--hidden-import=PIL',
        '--hidden-import=PIL._tkinter_finder',
        '--collect-all=customtkinter',
        '--clean',
        '--noconfirm',
    ])

if __name__ == "__main__":
    main() 