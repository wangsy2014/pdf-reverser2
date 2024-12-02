#!/bin/bash

# 清理不需要的文件
rm -f Dockerfile docker-compose.yml build.sh
rm -f mac_build.sh cross_build.sh create_release.sh easy_build.sh
rm -f auto_py_config.json setup.iss build.bat setup_git.sh
rm -rf .history/

# 重新初始化仓库
rm -rf .git
git init

# 添加核心文件
git add reverse_pdf_gui.py
git add reverse_pdf.py
git add pdf_icon.py
git add build_config.py
git add runtime_hook.py
git add requirements.txt
git add .gitignore
git add .github/workflows/build.yml

# 提交
git commit -m "Initial commit: Add PDF reverser tool with GitHub Actions"

# 设置远程仓库
git remote add origin git@github.com:wangsy2014/pdf-reverser2.git

# 设置主分支
git branch -M main

# 强制推送
git push -f origin main

echo "完成！请检查 GitHub 仓库。" 