# Resume Assistant Skill

> 智能简历助手技能包 - 为学生提供全方位求职支持的五个专业AI代理

[![Version](https://img.shields.io/badge/version-2.0.3-blue.svg)](releases/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)

---

## 🎯 快速开始

### 一行命令安装

```bash
# 将 resume-assistant.skill 文件拖入 Claude Code 对话框即可
```

### ⚠️ 重要提示

**首次使用前必须完成环境配置！** 详见 [INSTALLATION.md](INSTALLATION.md)

```bash
pip install fpdf2 python-docx openpyxl
mkdir -p /tmp/fonts && curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

---

## ✨ 核心功能

### 五个专业AI代理

| 代理 | 功能 | 触发词示例 |
|:---:|:---|:---|
| 🔍 **故事挖掘** | 发现被忽略的宝贵经历 | "我不知道写什么"<br>"帮我挖掘经历" |
| 💼 **职位推荐** | 基于背景推荐适合岗位 | "不知道找什么工作"<br>"适合什么岗位" |
| 📝 **简历优化** | 针对JD优化简历内容 | "帮我优化简历"<br>"投这个岗位" |
| 🎭 **模拟面试** | 面试练习+反向优化简历 | "模拟面试"<br>"帮我练习面试" |
| 📈 **能力提升** | 分析差距+制定提升计划 | "我想冲这个岗但能力不够" |

### 完整工作流

```mermaid
graph LR
    A[故事挖掘] --> B[职位推荐]
    B --> C[能力提升]
    C --> D[简历优化]
    D --> E[模拟面试]
    E -.反馈.-> D
```

---

## 🚀 使用场景

<details>
<summary><b>场景1：完全不知道从哪开始</b></summary>

```
用户："我不知道简历写什么，也不知道找什么工作"
助手：代理1（故事挖掘）→ 代理2（职位推荐）→ 代理3（简历优化）
输出：经历档案 + 岗位建议 + 初版简历
```
</details>

<details>
<summary><b>场景2：有目标但能力不够</b></summary>

```
用户："我想冲字节产品经理，但是应届生没经验"
助手：代理5（能力提升）→ 制定3-6个月提升计划
输出：差距分析 + 分阶段计划 + 学习资源 + 备选方案
```
</details>

<details>
<summary><b>场景3：有简历需要优化</b></summary>

```
用户："帮我根据这个JD优化简历"
助手：代理3（简历优化）→ 生成针对性简历
输出：优化版简历（PDF/DOCX/HTML）
```
</details>

<details>
<summary><b>场景4：准备面试</b></summary>

```
用户："下周要面试了，帮我练习"
助手：代理4（模拟面试）→ 提问、评估、反馈
输出：面试反馈报告 + 简历改进建议
```
</details>

---

## 📦 支持的输出格式

### 简历格式

| 格式 | 特点 | 推荐场景 |
|:---:|:---|:---|
| **PDF** ⭐ | 专业、跨平台兼容 | 正式投递 |
| **DOCX** | 可编辑、HR友好 | 需要进一步修改 |
| **HTML** | 响应式、支持深色模式 | 在线展示、打印 |

### 生成命令

```bash
# 切换到脚本目录
cd ~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant/scripts/current

# 生成 PDF（推荐）
python create_pdf_resume.py --data resume_data.json --output resume.pdf

# 生成 DOCX
python create_docx_resume.py output.docx --data resume_data.json

# 生成 HTML
python create_web_resume.py --data resume_data.json --output resume.html

# 生成能力提升追踪表（Excel）
python create_growth_tracker.py --data growth_plan.json --output growth_tracker.xlsx
```

---

## 🌟 独特优势

### 1. 故事挖掘的创新性
- ✅ 不只问"做过什么"，引导回忆被忽略的经历
- ✅ 发掘非传统经历（游戏公会管理、班级活动组织等）
- ✅ 识别可迁移技能

### 2. 能力提升的实用性
- ✅ 诚实评估差距（不盲目鼓励，不打击信心）
- ✅ 具体可执行计划（非空洞的"多学习"）
- ✅ 现实的Plan B方案

### 3. 模拟面试的反向优化
- ✅ 发现简历问题而非仅练习回答
- ✅ 如果答不上来，说明简历经不起追问
- ✅ 根据面试表现反向修改简历

---

## 📚 文档

| 文档 | 内容 |
|:---|:---|
| [INSTALLATION.md](INSTALLATION.md) | 详细安装指南（含平台特定说明） |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | 常见问题与解决方案 |
| [CHANGELOG.md](CHANGELOG.md) | 版本更新历史 |
| [releases/](releases/) | 历史发布说明 |

### 技能内部文档

- `resume-assistant-source/resume-assistant/SKILL.md` - 技能主文档
- `resume-assistant-source/resume-assistant/references/` - 代理实现指南
- `resume-assistant-source/resume-assistant/examples/` - 示例数据文件

---

## 🛠️ 技术栈

### 核心依赖

```
fpdf2>=2.7.0          # PDF 生成
python-docx>=1.1.0    # DOCX 生成
openpyxl>=3.1.0       # Excel 生成
```

### 系统要求

- **Python**: 3.7+
- **Claude Code**: 最新版本
- **磁盘空间**: 约 100MB（含字体文件）

---

## 📖 示例数据

技能包含完整的示例数据文件：

```
examples/
├── resume_data_example.json      # 完整简历数据示例
├── fresh_graduate_example.json   # 应届生示例
├── experienced_example.json      # 有经验者示例
├── growth_plan_example.json      # 能力提升计划示例
└── USAGE_GUIDE.md                # 使用指南
```

查看示例：
```bash
cat ~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant/examples/resume_data_example.json
```

---

## 🔧 高级用法

### JSON 数据格式

简历数据使用 JSON 格式，必填字段为 `name`：

```json
{
  "name": "张三",
  "title": "前端开发工程师",
  "phone": "138****8888",
  "email": "zhangsan@example.com",
  "location": "北京",
  "is_fresh_graduate": true,
  "summary": "个人简介...",
  "education": [...],
  "projects": [...],
  "experience": [...],
  "skills": [...]
}
```

完整格式请参考 `examples/resume_data_example.json`

---

## 📊 版本信息

### 当前版本：v2.0.3 (2026-02-01)

✅ **主要特性：**
- 修正 PDF 生成命令（fpdf2）
- 完整中文字体支持
- 新增详细文档（INSTALLATION.md, TROUBLESHOOTING.md）
- 优化脚本组织结构
- 添加完整示例数据

### 升级说明

从旧版本升级：

```bash
# 1. 备份数据
cp ~/.claude/skills/resume-assistant.skill ~/.claude/skills/resume-assistant.skill.bak

# 2. 下载新版本
# 从 GitHub releases 下载 resume-assistant.skill

# 3. 安装新版本
cp resume-assistant.skill ~/.claude/skills/

# 4. 更新依赖
pip install --upgrade fpdf2 python-docx openpyxl
```

查看完整更新日志：[CHANGELOG.md](CHANGELOG.md)

---

## 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

### 报告问题

1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. 搜索 [已有 Issues](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues)
3. 如未找到，[创建新 Issue](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues/new)

### Pull Request

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [Claude Code](https://claude.ai/claude-code) - AI 开发环境
- [fpdf2](https://github.com/py-pdf/fpdf2) - PDF 生成库
- [python-docx](https://github.com/python-openxml/python-docx) - DOCX 处理库
- [Noto Sans CJK](https://github.com/notofonts/noto-cjk) - 开源中文字体

---

## 📞 联系方式

- **GitHub Issues**: [提交问题](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues)
- **GitHub Discussions**: [参与讨论](https://github.com/Y1fe1-Yang/resume-assistant-skill/discussions)

---

## 🎯 快速链接

- [📥 安装指南](INSTALLATION.md) - 详细的安装步骤
- [🔧 故障排查](TROUBLESHOOTING.md) - 常见问题解决方案
- [📝 更新日志](CHANGELOG.md) - 版本历史
- [📦 发布说明](releases/) - 历史版本详情
- [💡 使用示例](resume-assistant-source/resume-assistant/examples/USAGE_GUIDE.md) - 实用案例

---

<p align="center">
  <b>开始使用</b>：安装技能后，直接对 Claude 说<br>
  <i>"帮我准备简历"</i> 或 <i>"我不知道找什么工作"</i>
</p>

<p align="center">
  <b>🎉 v2.0.3 已修复所有已知问题，可放心使用！</b>
</p>

---

**最后更新**: 2026-02-01 | **版本**: 2.0.3 | **状态**: ✅ 生产就绪
