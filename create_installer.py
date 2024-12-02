import os
import sys
from cx_Freeze import setup, Executable
import customtkinter

# 获取customtkinter包的路径
ctk_path = os.path.dirname(customtkinter.__file__)

# 依赖项
build_exe_options = {
    "packages": [
        "customtkinter",
        "tkinter",
        "PyPDF2",
        "PIL",
        "darkdetect",
        "typing",
    ],
    "includes": [
        "tkinter",
        "tkinter.filedialog",
        "PIL._tkinter_finder",
    ],
    "include_files": [
        "pdf_reverser.png",
        (ctk_path, "customtkinter"),
    ],
    "excludes": ["matplotlib", "numpy", "pandas"],
}

# 基础配置
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# 创建可执行文件
setup(
    name="PDF页面顺序反转工具",
    version="1.0",
    description="PDF页面顺序反转工具",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "reverse_pdf_gui.py",
            base=base,
            icon="pdf_reverser.png",
            target_name="PDF页面顺序反转工具",
        )
    ],
) 