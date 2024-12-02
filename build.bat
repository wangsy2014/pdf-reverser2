@echo off
echo 正在清理旧的构建文件...
rmdir /s /q build dist output

echo 正在生成图标...
python pdf_icon.py

echo 正在使用PyInstaller打包...
python build_config.py

echo 正在创建安装程序...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup.iss

echo 打包完成！
pause 