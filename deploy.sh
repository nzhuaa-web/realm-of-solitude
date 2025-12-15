#!/bin/bash

# 🚀 寂境王朝 - 一键部署脚本
# 支持多种部署平台：GitHub Pages、Netlify、Vercel

echo "🏰 寂境王朝 / Realm of Solitude - 部署工具"
echo "=========================================="

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 显示帮助信息
show_help() {
    echo -e "${BLUE}使用方法：${NC}"
    echo "  ./deploy.sh [选项]"
    echo ""
    echo -e "${BLUE}选项：${NC}"
    echo "  -g, --github    部署到GitHub Pages"
    echo "  -n, --netlify    部署到Netlify"
    echo "  -v, --vercel     部署到Vercel"
    echo "  -l, --local      启动本地服务器"
    echo "  -a, --all        部署到所有平台"
    echo "  -h, --help       显示此帮助信息"
    echo ""
    echo -e "${BLUE}示例：${NC}"
    echo "  ./deploy.sh --github    # 部署到GitHub Pages"
    echo "  ./deploy.sh --all       # 部署到所有平台"
    echo "  ./deploy.sh --local     # 启动本地服务器"
}

# 检查文件完整性
check_files() {
    echo -e "${YELLOW}检查项目文件完整性...${NC}"
    
    local required_files=("survival_game.html" "README.md" "package.json")
    local missing_files=()
    
    for file in "${required_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            missing_files+=("$file")
        fi
    done
    
    if [[ ${#missing_files[@]} -gt 0 ]]; then
        echo -e "${RED}错误：缺少必要文件：${NC}"
        for file in "${missing_files[@]}"; do
            echo "  - $file"
        done
        exit 1
    fi
    
    echo -e "${GREEN}✓ 所有必要文件都存在${NC}"
}

# 部署到GitHub Pages
deploy_github() {
    echo -e "${BLUE}部署到GitHub Pages...${NC}"
    
    # 检查是否在Git仓库中
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo -e "${RED}错误：当前目录不是Git仓库${NC}"
        echo "请先初始化Git仓库："
        echo "  git init"
        echo "  git add ."
        echo "  git commit -m 'Initial commit'"
        return 1
    fi
    
    # 检查是否有远程仓库
    if ! git remote get-url origin > /dev/null 2>&1; then
        echo -e "${RED}错误：没有设置远程仓库${NC}"
        echo "请先添加远程仓库："
        echo "  git remote add origin [你的仓库URL]"
        return 1
    fi
    
    # 推送代码
    echo "推送代码到GitHub..."
    git push origin main
    
    echo -e "${GREEN}✓ 代码已推送到GitHub${NC}"
    echo ""
    echo -e "${YELLOW}下一步：${NC}"
    echo "1. 访问 https://github.com/[用户名]/[仓库名]/settings/pages"
    echo "2. 在'Source'部分选择'GitHub Actions'"
    echo "3. 等待部署完成，访问 https://[用户名].github.io/[仓库名]"
}

# 部署到Netlify
deploy_netlify() {
    echo -e "${BLUE}部署到Netlify...${NC}"
    
    # 检查是否安装了Netlify CLI
    if ! command -v netlify &> /dev/null; then
        echo -e "${RED}错误：未安装Netlify CLI${NC}"
        echo "请先安装："
        echo "  npm install -g netlify-cli"
        return 1
    fi
    
    # 检查是否已登录
    if ! netlify status &> /dev/null; then
        echo "请先登录Netlify："
        netlify login
    fi
    
    # 部署
    echo "开始部署到Netlify..."
    netlify deploy --prod --dir=.
    
    echo -e "${GREEN}✓ 部署完成${NC}"
}

# 部署到Vercel
deploy_vercel() {
    echo -e "${BLUE}部署到Vercel...${NC}"
    
    # 检查是否安装了Vercel CLI
    if ! command -v vercel &> /dev/null; then
        echo -e "${RED}错误：未安装Vercel CLI${NC}"
        echo "请先安装："
        echo "  npm install -g vercel"
        return 1
    fi
    
    # 部署
    echo "开始部署到Vercel..."
    vercel --prod
    
    echo -e "${GREEN}✓ 部署完成${NC}"
}

# 启动本地服务器
start_local() {
    echo -e "${BLUE}启动本地服务器...${NC}"
    
    # 检查是否有Python
    if command -v python3 &> /dev/null; then
        echo "使用Python服务器 (端口 8000)"
        python3 -m http.server 8000 &
        PYTHON_PID=$!
        echo -e "${GREEN}服务器已启动：http://localhost:8000${NC}"
        echo "按Ctrl+C停止服务器"
        wait $PYTHON_PID
    elif command -v node &> /dev/null; then
        echo "使用Node.js服务器 (端口 3000)"
        npx serve . -p 3000 &
        NODE_PID=$!
        echo -e "${GREEN}服务器已启动：http://localhost:3000${NC}"
        echo "按Ctrl+C停止服务器"
        wait $NODE_PID
    else
        echo -e "${RED}错误：未找到Python或Node.js${NC}"
        echo "请安装以下之一："
        echo "  - Python 3: https://python.org"
        echo "  - Node.js: https://nodejs.org"
        return 1
    fi
}

# 显示部署信息
show_deploy_info() {
    echo ""
    echo -e "${BLUE}🎮 寂境王朝 - 部署完成${NC}"
    echo "=========================================="
    echo -e "${GREEN}游戏已成功部署！${NC}"
    echo ""
    echo -e "${YELLOW}游戏特色：${NC}"
    echo "  • Nopoly极简风格"
    echo "  • 轻量策略生存玩法"
    echo "  • 昼夜循环系统"
    echo "  • 王令策略选择"
    echo "  • 灵光能量系统"
    echo ""
    echo -e "${YELLOW}游戏操作：${NC}"
    echo "  1. 选择3个王令开始游戏"
    echo "  2. 白天建造，夜晚防御"
    echo "  3. 使用技能对抗虚空生物"
    echo "  4. 生存10天完成关卡"
    echo ""
    echo -e "${YELLOW}技术信息：${NC}"
    echo "  • 纯HTML5/CSS3/JavaScript"
    echo "  • 响应式设计"
    echo "  • 无外部依赖"
    echo "  • 支持离线游玩"
    echo ""
}

# 主函数
main() {
    # 检查参数
    if [[ $# -eq 0 ]]; then
        show_help
        exit 0
    fi
    
    # 解析参数
    case $1 in
        -g|--github)
            check_files
            deploy_github
            show_deploy_info
            ;;
        -n|--netlify)
            check_files
            deploy_netlify
            show_deploy_info
            ;;
        -v|--vercel)
            check_files
            deploy_vercel
            show_deploy_info
            ;;
        -l|--local)
            check_files
            start_local
            ;;
        -a|--all)
            check_files
            echo -e "${BLUE}部署到所有平台...${NC}"
            deploy_github
            deploy_netlify
            deploy_vercel
            show_deploy_info
            ;;
        -h|--help)
            show_help
            ;;
        *)
            echo -e "${RED}错误：未知选项 '$1'${NC}"
            show_help
            exit 1
            ;;
    esac
}

# 运行主函数
main "$@"