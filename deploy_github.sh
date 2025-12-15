#!/bin/bash

# 🚀 寂境王朝 - GitHub Pages 部署脚本
# 作者: Litazhu
# 描述: 自动化GitHub Pages部署流程

echo "🏰 寂境王朝 GitHub Pages 部署工具"
echo "=================================="

# 检查Git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ Git未安装，请先安装Git"
    echo "下载地址: https://git-scm.com/"
    exit 1
fi

# 获取项目信息
PROJECT_NAME="realm-of-solitude"
GITHUB_USERNAME=""

# 询问GitHub用户名
read -p "请输入你的GitHub用户名: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

echo ""
echo "📋 部署信息汇总:"
echo "   项目名称: $PROJECT_NAME"
echo "   GitHub用户: $GITHUB_USERNAME"
echo "   部署地址: https://$GITHUB_USERNAME.github.io/$PROJECT_NAME"
echo ""

# 自动确认部署
CONFIRM="y"
echo "自动确认开始部署..."

# 步骤1: 初始化Git仓库
echo "📦 步骤1: 初始化Git仓库..."
git init
git add .
git commit -m "初始提交: 寂境王朝 Nopoly风格生存策略游戏"

# 步骤2: 创建GitHub仓库
echo "🌐 步骤2: 创建GitHub远程仓库..."
GITHUB_URL="https://github.com/$GITHUB_USERNAME/$PROJECT_NAME.git"
git branch -M main
git remote add origin $GITHUB_URL

# 步骤3: 推送代码
echo "🚀 步骤3: 推送代码到GitHub..."
git push -u origin main

echo ""
echo "✅ 代码推送完成!"
echo ""

# 步骤4: 提供后续操作指南
echo "📋 后续手动操作步骤:"
echo "1. 访问 https://github.com/$GITHUB_USERNAME/$PROJECT_NAME"
echo "2. 点击 Settings → Pages"
echo "3. Source选择 'GitHub Actions'"
echo "4. 保存设置，等待自动部署"
echo "5. 访问 https://$GITHUB_USERNAME.github.io/$PROJECT_NAME"
echo ""

# 步骤5: 检查部署状态
echo "⏳ 部署状态检查:"
echo "- 部署通常需要1-5分钟完成"
echo "- 在仓库的 'Actions' 选项卡查看进度"
echo "- 绿色勾号表示部署成功"
echo ""

echo "🎮 游戏功能预览:"
echo "- Nopoly极简风格界面"
echo "- 昼夜循环生存系统"
echo "- 王令策略选择"
echo "- 灵光能量资源管理"
echo "- 英雄技能战斗系统"
echo ""

echo "🌐 技术特性:"
echo "- 纯HTML/CSS/JavaScript实现"
echo "- 响应式设计，支持移动端"
echo "- 无需服务器，静态托管"
echo "- GitHub Pages自动HTTPS"
echo ""

echo "🎯 部署完成! 开始你的寂境王朝重建之旅吧!"