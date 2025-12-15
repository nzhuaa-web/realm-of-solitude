# 🚀 寂境王朝 - 完整部署指南

## 📋 项目概览

**项目名称**: 寂境王朝 / Realm of Solitude  
**类型**: HTML5 轻量生存策略游戏  
**技术栈**: 纯HTML/CSS/JavaScript，无外部依赖  
**文件大小**: ~82KB (单文件部署)  
**兼容性**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

## 🎯 部署目标

- ✅ **GitHub Pages** - 免费静态托管
- ✅ **Netlify** - CDN加速，一键部署  
- ✅ **Vercel** - 边缘计算，快速部署
- ✅ **本地服务器** - 开发测试环境
- ✅ **自定义域名** - 支持HTTPS

## 📁 项目文件结构

```
realm-of-solitude/
├── 📄 survival_game.html          # 主游戏文件 (82KB)
├── 📄 slg.py                       # Python后端逻辑 (8KB)
├── 📄 slg_ui.py                    # Python GUI版本 (14KB)
├── 📄 package.json                 # Node.js项目配置
├── 📄 netlify.toml                 # Netlify部署配置
├── 📄 vercel.json                  # Vercel部署配置
├── 📄 deploy.sh                    # 一键部署脚本
├── 📄 test_deployment.html         # 部署测试页面
├── 📄 README.md                    # 项目说明文档
├── 📄 DEPLOYMENT.md                # 本部署指南
└── 📁 .github/workflows/
    └── 📄 deploy.yml               # GitHub Actions配置
```

## 🚀 快速部署方案

### 方案一：GitHub Pages (推荐)

**优势**: 免费、稳定、支持自定义域名、自动HTTPS

#### 部署步骤:

1. **创建GitHub仓库**
   ```bash
   # 初始化仓库
   git init
   git add .
   git commit -m "Initial commit: Realm of Solitude game"
   
   # 添加远程仓库
   git remote add origin https://github.com/[用户名]/[仓库名].git
   git push -u origin main
   ```

2. **启用GitHub Pages**
   - 访问仓库 Settings > Pages
   - Source 选择 "GitHub Actions"
   - 保存设置

3. **自动部署**
   - 每次推送到main分支会自动触发部署
   - 访问地址: `https://[用户名].github.io/[仓库名]`

#### 自定义域名:
```
# 在仓库根目录创建CNAME文件
echo "your-domain.com" > CNAME

# DNS设置 (在域名提供商处)
CNAME your-domain.com -> [用户名].github.io
```

### 方案二：Netlify (一键部署)

**优势**: 极速CDN、自动HTTPS、环境变量管理

#### 部署步骤:

1. **Web界面部署**
   - 访问 [netlify.com](https://netlify.com)
   - 拖拽项目文件夹到部署区域
   - 自动生成部署链接

2. **Git集成部署**
   - 连接GitHub仓库
   - 选择部署分支 (main)
   - 自动构建和部署

3. **CLI部署**
   ```bash
   # 安装Netlify CLI
   npm install -g netlify-cli
   
   # 登录和部署
   netlify login
   netlify deploy --prod
   ```

#### 环境配置:
```toml
# netlify.toml 已配置
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/survival_game.html"
```

### 方案三：Vercel (快速部署)

**优势**: 边缘网络、自动SSL、预览部署

#### 部署步骤:

1. **CLI部署**
   ```bash
   # 安装Vercel CLI
   npm install -g vercel
   
   # 一键部署
   vercel --prod
   ```

2. **Git集成部署**
   - 导入GitHub仓库到Vercel
   - 自动检测配置并部署
   - 支持预览分支部署

3. **环境变量**
   ```json
   // vercel.json 已配置
   {
     "env": {
       "GAME_NAME": "寂境王朝",
       "GAME_VERSION": "1.0.0"
     }
   }
   ```

### 方案四：本地服务器 (开发测试)

#### Python服务器:
```bash
# Python 3.x
python3 -m http.server 8000
# 访问 http://localhost:8000
```

#### Node.js服务器:
```bash
# 使用serve包
npx serve . -p 3000
# 访问 http://localhost:3000
```

#### 一键脚本:
```bash
# 使用部署脚本
chmod +x deploy.sh
./deploy.sh --local
```

## 🔧 部署脚本使用

### deploy.sh 功能:

```bash
# 显示帮助
./deploy.sh --help

# 部署到GitHub Pages
./deploy.sh --github

# 部署到Netlify
./deploy.sh --netlify

# 部署到Vercel
./deploy.sh --vercel

# 启动本地服务器
./deploy.sh --local

# 部署到所有平台
./deploy.sh --all
```

### 脚本功能:
- ✅ 文件完整性检查
- ✅ 环境依赖检测
- ✅ 自动部署流程
- ✅ 错误处理和提示
- ✅ 多平台支持

## 🧪 部署测试

### 测试页面:
访问 `test_deployment.html` 进行完整测试:

```bash
# 启动测试服务器
python3 -m http.server 8000
# 访问 http://localhost:8000/test_deployment.html
```

### 测试项目:
- ✅ 浏览器兼容性检测
- ✅ JavaScript执行测试
- ✅ CSS3动画支持
- ✅ 游戏文件加载测试
- ✅ 资源完整性验证

## ⚙️ 技术配置详情

### GitHub Actions 配置:
```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages
on: [push, pull_request]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
      - uses: actions/deploy-pages@v4
```

### Netlify 配置:
```toml
# netlify.toml
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/survival_game.html"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
```

### Vercel 配置:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "survival_game.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/survival_game.html"
    }
  ]
}
```

## 🔍 故障排除

### 常见问题:

**Q: 部署后显示空白页面？**
A: 检查入口文件配置，确保 `survival_game.html` 是主文件

**Q: GitHub Pages 404错误？**
A: 检查仓库设置，确保Pages已启用，分支选择正确

**Q: 资源加载失败？**
A: 检查文件路径，所有资源应使用相对路径

**Q: 移动端显示异常？**
A: 游戏针对桌面优化，建议横屏模式游玩

**Q: 部署脚本权限错误？**
A: 执行 `chmod +x deploy.sh` 添加执行权限

### 调试模式:
```javascript
// 在浏览器控制台启用调试
localStorage.setItem('debug', 'true')
location.reload()
```

## 📊 性能优化

### 部署优化:
- ✅ 单文件部署，减少HTTP请求
- ✅ CSS内联，避免样式表加载
- ✅ 图片使用Emoji和CSS绘制
- ✅ 轻量级JavaScript逻辑
- ✅ 支持Service Worker (PWA)

### CDN优化:
- ✅ Netlify全球CDN
- ✅ Vercel边缘网络
- ✅ GitHub Pages全球分发
- ✅ 自动Gzip压缩
- ✅ 浏览器缓存策略

## 🔒 安全配置

### HTTPS强制:
所有平台自动启用HTTPS:
- GitHub Pages: 自动SSL证书
- Netlify: Let's Encrypt自动续期
- Vercel: 边缘网络SSL

### 安全头设置:
```
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

## 🌐 域名配置

### 自定义域名步骤:

1. **购买域名** (Namecheap, GoDaddy等)
2. **配置DNS记录**
3. **平台域名设置**
4. **SSL证书验证**

### DNS配置示例:
```
# GitHub Pages
CNAME your-domain.com -> username.github.io

# Netlify
CNAME your-domain.com -> your-site.netlify.app

# Vercel
CNAME your-domain.com -> cname.vercel-dns.com
```

## 📈 监控和分析

### 可选集成:
- **Google Analytics**: 用户行为分析
- **Hotjar**: 用户交互热图
- **Sentry**: 错误监控
- **UptimeRobot**: 可用性监控

### 集成方法:
```html
<!-- 在survival_game.html中添加 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🔄 更新和维护

### 版本更新:
```bash
# 更新游戏内容后
git add .
git commit -m "feat: 新增关卡系统"
git push origin main

# 自动触发部署
```

### 回滚部署:
```bash
# GitHub Pages
git revert HEAD
git push origin main

# Netlify/Vercel
在控制台选择之前的部署版本
```

## 🎯 最佳实践

### 部署前检查清单:
- [ ] 所有文件路径使用相对路径
- [ ] 测试所有浏览器兼容性
- [ ] 验证资源加载正常
- [ ] 检查移动端适配
- [ ] 测试游戏功能完整性

### 性能优化建议:
- 启用Gzip压缩
- 配置浏览器缓存
- 使用CDN加速
- 优化图片和资源
- 减少JavaScript阻塞

## 📞 技术支持

### 问题反馈:
- GitHub Issues: 功能请求和Bug报告
- 邮箱支持: 技术问题咨询
- 文档更新: 部署指南维护

### 社区资源:
- Discord频道: 实时技术支持
- 文档Wiki: 详细使用指南
- 示例项目: 部署案例参考

---

## 🎮 开始部署！

选择最适合你的部署方案，让《寂境王朝》在公网运行起来！

**推荐部署流程:**
1. 使用 `./deploy.sh --local` 本地测试
2. 使用 `./deploy.sh --github` 部署到GitHub Pages
3. 配置自定义域名 (可选)
4. 分享游戏链接给朋友体验

**游戏链接示例:**
- GitHub Pages: `https://yourname.github.io/realm-of-solitude`
- Netlify: `https://your-game.netlify.app`
- Vercel: `https://your-game.vercel.app`

---

*🎯 部署成功！现在你可以与全世界分享你的寂境王朝了！*