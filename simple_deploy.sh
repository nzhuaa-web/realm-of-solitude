#!/bin/bash

# 🚀 简化的GitHub Pages部署脚本
echo "🏰 寂境王朝 - 简化部署工具"
echo "=================================="

# 设置变量
GITHUB_USER="litazhu"
REPO_NAME="realm-of-solitude"
GITHUB_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

# 检查Git状态
echo "📊 检查Git状态..."
git status

# 添加远程仓库（如果不存在）
echo "🌐 配置远程仓库..."
git remote remove origin 2>/dev/null
git remote add origin $GITHUB_URL

# 推送代码
echo "🚀 推送代码到GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ 代码推送完成!"
echo ""

# 显示后续步骤
echo "📋 后续手动操作:"
echo "1. 访问 https://github.com/$GITHUB_USER/$REPO_NAME"
echo "2. Settings → Pages → Source选择 'GitHub Actions'"
echo "3. 保存设置，等待自动部署"
echo "4. 访问 https://$GITHUB_USER.github.io/$REPO_NAME"
echo ""
echo "⏳ 部署通常需要1-5分钟完成"
echo "🎮 游戏即将上线!"