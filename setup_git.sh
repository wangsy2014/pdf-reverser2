#!/bin/bash

# 配置 Git 用户信息
echo "配置 Git 用户信息..."
git config --global user.name "wangsy2014"
git config --global user.email "你的邮箱"

# 设置默认分支名
git config --global init.defaultBranch main

# 生成 SSH 密钥
echo "生成 SSH 密钥..."
ssh-keygen -t ed25519 -C "你的邮箱"

# 启动 ssh-agent 并添加密钥
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 显示公钥内容
echo "请复制以下公钥内容到 GitHub："
cat ~/.ssh/id_ed25519.pub

# 等待用户添加密钥到 GitHub
echo "请将上面的公钥添加到 GitHub 后按回车继续..."
read

# 测试 SSH 连接
echo "测试 SSH 连接..."
ssh -T git@github.com

# 修改远程仓库 URL
echo "修改远程仓库 URL..."
git remote set-url origin git@github.com:wangsy2014/pdf-reverser2.git

echo "设置完成！现在可以免密推送代码了。" 