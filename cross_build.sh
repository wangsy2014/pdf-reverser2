#!/bin/bash

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install pyinstaller-cross customtkinter PyPDF2 pillow

# 创建打包配置
cat > cross_config.spec << EOL
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['reverse_pdf_gui.py'],
             pathex=['.'],
             binaries=[],
             datas=[('pdf_reverser.png', '.')],
             hiddenimports=['customtkinter', 'tkinter', 'PIL', 'PIL._tkinter_finder'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PDF页面顺序反转工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='pdf_reverser.png')
EOL

# 执行跨平台打包
pyinstaller-cross --platform win64 cross_config.spec

echo "打包完成！" 