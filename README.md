# 简历助手 Resume Assistant Skill

<div align="center">

[![GitHub release](https://img.shields.io/github/v/release/Y1fe1-Yang/resume-assistant-skill)](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)
[![License](https://img.shields.io/github/license/Y1fe1-Yang/resume-assistant-skill)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Skill-7C3AED)](https://claude.ai/code)

**[中文](#中文) | [English](#english)**

</div>

---

<h2 id="中文">🇨🇳 中文文档</h2>

<div align="right">

**[English Version ⬇️](#english)**

</div>

### 📖 简介

智能简历助手，通过五个专业 AI 代理提供全流程求职支持。为 [Claude Code](https://claude.ai/code) 设计的技能包。

### 📦 安装

```bash
# 下载最新版本
curl -L -O https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest/download/resume-assistant-skill.skill

# 安装技能包
claude skills install resume-assistant-skill.skill
```

**环境配置**（首次使用）:
```bash
pip install fpdf2 python-docx openpyxl
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### ✨ 功能特点

#### 五个专业 AI 代理

- **🔍 故事挖掘代理**
  引导式对话，帮助发现被忽略的有价值经历和可迁移技能

- **💼 职位推荐代理**
  基于背景和兴趣，推荐合适的职位方向

- **📝 简历优化代理**
  根据目标岗位 JD 针对性优化简历，提升关键词匹配度

- **🎭 模拟面试代理**
  模拟真实面试场景，提供详细反馈并反向优化简历

- **📈 能力提升代理**
  分析技能差距，制定具体可执行的提升计划

#### 输出格式

- 📄 **PDF** - 专业格式，适合正式投递
- 📝 **DOCX** - 可编辑格式，便于进一步修改
- 🌐 **HTML** - 现代响应式设计，支持深色模式
- 📊 **Excel** - 能力提升追踪表，包含里程碑

### 🚀 快速开始

安装后，直接与 Claude Code 对话：

```
"帮我写简历"              # 创建简历
"优化这份简历"            # 优化现有简历
"模拟面试"               # 面试练习
"职业规划"               # 职业规划
"我想冲XX岗位但能力不够"   # 技能差距分析
```

### 🎯 使用场景

| 场景 | 使用代理 | 输出 |
|------|---------|------|
| 首次写简历 | 故事挖掘 → 简历优化 | 打磨后的简历 |
| 岗位投递 | 简历优化 | 定制化简历 |
| 面试准备 | 模拟面试 | 练习反馈 |
| 职业发展 | 职位推荐 → 能力提升 | 发展计划 |
| 完整求职辅导 | 全部 5 个代理 | 端到端支持 |

### 💡 完整工作流程

```
1️⃣ 故事挖掘
   "我不知道简历写什么" → 引导对话 → 《经历档案》

2️⃣ 职位推荐
   基于档案 → 匹配分析 → 《职位推荐报告》

3️⃣ 简历优化
   "帮我优化简历，投XX岗位" + JD → 《优化版简历》(JSON)

4️⃣ 文件生成
   使用脚本 → PDF/DOCX/HTML 简历

5️⃣ 模拟面试
   基于简历 → 模拟提问 → 《面试反馈》+ 简历改进建议

6️⃣ 能力提升（可选）
   如果能力不足 → 差距分析 → 《提升规划》+ Excel 追踪表
```

### 📚 文档

- **[SKILL.md](SKILL.md)** - 完整的技能文档（供 Claude 使用）
- **[skillmap.json](skillmap.json)** - 技能元数据
- **[examples/](examples/)** - 示例数据文件
- **[references/](references/)** - 参考文档（写作指南、行业关键词等）
- **[Releases](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)** - 下载打包文件

### 📋 系统要求

- ✅ **Claude Code** 已安装
- ✅ **Python 3.7+** 用于脚本执行
- ✅ **Python 包**: `fpdf2`, `python-docx`, `openpyxl`
- ✅ **字体**: NotoSansSC（用于中文 PDF 生成）

### 🔧 故障排查

**PDF 生成失败**:
```bash
# 重新下载字体
rm -f /tmp/fonts/NotoSansSC.ttf
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**脚本找不到**:
```bash
# 确保在正确目录
cd ~/.claude/skills/resume-assistant
```

更多问题请查看 [references/troubleshooting.md](references/troubleshooting.md)

### 🌟 特色亮点

- ✨ **中文优化** - 专为中国求职市场设计
- ✨ **五大代理** - 覆盖求职全流程
- ✨ **多种格式** - PDF/DOCX/HTML/Excel 一应俱全
- ✨ **智能匹配** - 根据 JD 自动优化关键词
- ✨ **实战演练** - 模拟真实面试场景
- ✨ **持续成长** - 制定可执行的提升计划

### 📄 开源协议

[MIT](LICENSE) - 免费使用，欢迎贡献

### 🔗 相关链接

- **仓库**: https://github.com/Y1fe1-Yang/resume-assistant-skill
- **最新版本**: https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest
- **Claude Code**: https://claude.ai/code
- **问题反馈**: https://github.com/Y1fe1-Yang/resume-assistant-skill/issues

### 📊 版本信息

- **当前版本**: 2.1.0
- **质量评分**: A (9.3/10)
- **最后更新**: 2026-02-01

---

<h2 id="english">🇬🇧 English Documentation</h2>

<div align="right">

**[中文版本 ⬆️](#中文)**

</div>

### 📖 Introduction

An AI-powered resume assistant with 5 specialized agents for Chinese job seekers, designed for [Claude Code](https://claude.ai/code).

### 📦 Installation

```bash
# Download the latest release
curl -L -O https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest/download/resume-assistant-skill.skill

# Install the skill
claude skills install resume-assistant-skill.skill
```

**Environment setup** (first time only):
```bash
pip install fpdf2 python-docx openpyxl
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### ✨ Features

#### Five Specialized AI Agents

- **🔍 Story Mining Agent**
  Discover overlooked experiences and highlight transferable skills through guided conversations

- **💼 Job Recommendation Agent**
  Match suitable positions based on background and interests

- **📝 Resume Optimization Agent**
  Tailor content to specific job descriptions with keyword optimization

- **🎭 Mock Interview Agent**
  Practice interviews with realistic questions and constructive feedback

- **📈 Growth Planning Agent**
  Analyze skill gaps and create actionable development plans

#### Output Formats

- 📄 **PDF** - Professional format for formal applications
- 📝 **DOCX** - Editable format for further customization
- 🌐 **HTML** - Modern responsive design with dark mode support
- 📊 **Excel** - Growth tracking spreadsheet with milestones

### 🚀 Quick Start

After installation, simply chat with Claude Code:

```
"帮我写简历"              # Create a resume
"优化这份简历"            # Optimize existing resume
"模拟面试"               # Practice interview
"职业规划"               # Career planning
"我想冲XX岗位但能力不够"   # Skill gap analysis
```

### 🎯 Use Cases

| Scenario | Agents Used | Output |
|----------|-------------|--------|
| First-time resume | Story Mining → Resume Optimization | Polished resume |
| Job application | Resume Optimization | Tailored resume |
| Interview prep | Mock Interview | Practice feedback |
| Career development | Job Recommendation → Growth Planning | Development plan |
| Complete job search | All 5 agents | End-to-end support |

### 💡 Complete Workflow

```
1️⃣ Story Mining
   Discover experiences → Guided conversation → Experience profile

2️⃣ Job Recommendation
   Based on profile → Matching analysis → Job recommendation report

3️⃣ Resume Optimization
   "Optimize for XX position" + JD → Optimized resume (JSON)

4️⃣ File Generation
   Use scripts → PDF/DOCX/HTML resume

5️⃣ Mock Interview
   Based on resume → Mock questions → Interview feedback + Resume improvements

6️⃣ Growth Planning (Optional)
   If skills lacking → Gap analysis → Growth plan + Excel tracker
```

### 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill documentation (for Claude)
- **[skillmap.json](skillmap.json)** - Skill metadata
- **[examples/](examples/)** - Sample data files
- **[references/](references/)** - Reference docs (writing guide, industry keywords, etc.)
- **[Releases](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)** - Download packaged skill

### 📋 Requirements

- ✅ **Claude Code** installed
- ✅ **Python 3.7+** for script execution
- ✅ **Python packages**: `fpdf2`, `python-docx`, `openpyxl`
- ✅ **Font**: NotoSansSC (for Chinese PDF generation)

### 🔧 Troubleshooting

**PDF generation fails**:
```bash
# Re-download font
rm -f /tmp/fonts/NotoSansSC.ttf
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**Script not found**:
```bash
# Ensure correct directory
cd ~/.claude/skills/resume-assistant
```

For more issues, see [references/troubleshooting.md](references/troubleshooting.md)

### 🌟 Highlights

- ✨ **Chinese-optimized** - Designed for Chinese job market
- ✨ **Five agents** - Complete job search coverage
- ✨ **Multiple formats** - PDF/DOCX/HTML/Excel support
- ✨ **Smart matching** - Auto-optimize keywords based on JD
- ✨ **Real practice** - Realistic interview simulation
- ✨ **Continuous growth** - Actionable improvement plans

### 📄 License

[MIT](LICENSE) - Free to use, contributions welcome

### 🔗 Links

- **Repository**: https://github.com/Y1fe1-Yang/resume-assistant-skill
- **Latest Release**: https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest
- **Claude Code**: https://claude.ai/code
- **Issues**: https://github.com/Y1fe1-Yang/resume-assistant-skill/issues

### 📊 Version Info

- **Current Version**: 2.1.0
- **Quality Score**: A (9.3/10)
- **Last Updated**: 2026-02-01

---

<div align="center">

**为 Claude Code 量身打造 | Made for Claude Code**

</div>
