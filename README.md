# 简历助手 Resume Assistant Skill

[![GitHub release](https://img.shields.io/github/v/release/Y1fe1-Yang/resume-assistant-skill)](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)
[![License](https://img.shields.io/github/license/Y1fe1-Yang/resume-assistant-skill)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Skill-7C3AED)](https://claude.ai/code)

智能简历助手，通过五个专业 AI 代理提供全流程求职支持。

An AI-powered resume assistant with 5 specialized agents for Chinese job seekers, designed for [Claude Code](https://claude.ai/code).

---

## 📦 安装 Installation

```bash
# 下载最新版本 Download the latest release
curl -L -O https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest/download/resume-assistant-skill.skill

# 安装技能包 Install the skill
claude skills install resume-assistant-skill.skill
```

**环境配置**（首次使用）/ **Environment setup** (first time only):
```bash
pip install fpdf2 python-docx openpyxl
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

---

## ✨ 功能特点 Features

### 五个专业 AI 代理 Five Specialized AI Agents

- **🔍 故事挖掘代理** Story Mining Agent
  引导式对话，帮助发现被忽略的有价值经历和可迁移技能
  *Discover overlooked experiences and highlight transferable skills*

- **💼 职位推荐代理** Job Recommendation Agent
  基于背景和兴趣，推荐合适的职位方向
  *Match suitable positions based on background and interests*

- **📝 简历优化代理** Resume Optimization Agent
  根据目标岗位 JD 针对性优化简历，提升关键词匹配度
  *Tailor content to specific job descriptions with keyword optimization*

- **🎭 模拟面试代理** Mock Interview Agent
  模拟真实面试场景，提供详细反馈并反向优化简历
  *Practice interviews with realistic questions and constructive feedback*

- **📈 能力提升代理** Growth Planning Agent
  分析技能差距，制定具体可执行的提升计划
  *Analyze skill gaps and create actionable development plans*

### 输出格式 Output Formats

- 📄 **PDF** - 专业格式，适合正式投递 / *Professional format for formal applications*
- 📝 **DOCX** - 可编辑格式，便于进一步修改 / *Editable format for further customization*
- 🌐 **HTML** - 现代响应式设计，支持深色模式 / *Modern responsive design with dark mode*
- 📊 **Excel** - 能力提升追踪表，包含里程碑 / *Growth tracking spreadsheet with milestones*

---

## 🚀 快速开始 Quick Start

安装后，直接与 Claude Code 对话：

*After installation, simply chat with Claude Code:*

```
"帮我写简历"              # 创建简历 Create a resume
"优化这份简历"            # 优化现有简历 Optimize existing resume
"模拟面试"               # 面试练习 Practice interview
"职业规划"               # 职业规划 Career planning
"我想冲XX岗位但能力不够"   # 技能差距分析 Skill gap analysis
```

---

## 🎯 使用场景 Use Cases

| 场景 Scenario | 使用代理 Agents Used | 输出 Output |
|--------------|---------------------|------------|
| 首次写简历<br>*First-time resume* | 故事挖掘 → 简历优化<br>*Story Mining → Resume Optimization* | 打磨后的简历<br>*Polished resume* |
| 岗位投递<br>*Job application* | 简历优化<br>*Resume Optimization* | 定制化简历<br>*Tailored resume* |
| 面试准备<br>*Interview prep* | 模拟面试<br>*Mock Interview* | 练习反馈<br>*Practice feedback* |
| 职业发展<br>*Career development* | 职位推荐 → 能力提升<br>*Job Recommendation → Growth Planning* | 发展计划<br>*Development plan* |
| 完整求职辅导<br>*Complete job search* | 全部 5 个代理<br>*All 5 agents* | 端到端支持<br>*End-to-end support* |

---

## 💡 工作流程示例 Workflow Example

### 完整求职流程 Complete Job Search Flow

```
1️⃣ 故事挖掘 Story Mining
   "我不知道简历写什么" → 引导对话 → 《经历档案》

2️⃣ 职位推荐 Job Recommendation
   基于档案 → 匹配分析 → 《职位推荐报告》

3️⃣ 简历优化 Resume Optimization
   "帮我优化简历，投XX岗位" + JD → 《优化版简历》(JSON)

4️⃣ 文件生成 File Generation
   使用脚本 → PDF/DOCX/HTML 简历

5️⃣ 模拟面试 Mock Interview
   基于简历 → 模拟提问 → 《面试反馈》+ 简历改进建议

6️⃣ 能力提升 Growth Planning (可选)
   如果能力不足 → 差距分析 → 《提升规划》+ Excel 追踪表
```

---

## 📚 文档 Documentation

- **[SKILL.md](SKILL.md)** - 完整的技能文档（供 Claude 使用）/ *Complete skill documentation (for Claude)*
- **[skillmap.json](skillmap.json)** - 技能元数据 / *Skill metadata*
- **[examples/](examples/)** - 示例数据文件 / *Sample data files*
- **[references/](references/)** - 参考文档（写作指南、行业关键词等）/ *Reference docs*
- **[Releases](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)** - 下载打包文件 / *Download packaged skill*

---

## 📋 系统要求 Requirements

- ✅ **Claude Code** 已安装 / *installed*
- ✅ **Python 3.7+** 用于脚本执行 / *for script execution*
- ✅ **Python 包** / *packages*: `fpdf2`, `python-docx`, `openpyxl`
- ✅ **字体** / *Font*: NotoSansSC（用于中文 PDF 生成 / *for Chinese PDF generation*）

---

## 🔧 故障排查 Troubleshooting

### 常见问题 Common Issues

**PDF 生成失败** / *PDF generation fails*:
```bash
# 重新下载字体 Re-download font
rm -f /tmp/fonts/NotoSansSC.ttf
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**脚本找不到** / *Script not found*:
```bash
# 确保在正确目录 Ensure correct directory
cd ~/.claude/skills/resume-assistant
```

更多问题请查看 [references/troubleshooting.md](references/troubleshooting.md)

*For more issues, see [references/troubleshooting.md](references/troubleshooting.md)*

---

## 📄 开源协议 License

[MIT](LICENSE) - 免费使用，欢迎贡献 / *Free to use, contributions welcome*

---

## 🙏 致谢 Acknowledgments

本技能包为中国求职者提供全面的职业辅助，通过以下方式实现：

*This skill provides comprehensive career assistance for Chinese job seekers through:*

- 🤖 AI 驱动的对话式引导 / *AI-powered conversational guidance*
- 📝 简历写作领域专业知识 / *Domain expertise in resume writing*
- 🔧 可靠的文档生成脚本 / *Reliable document generation scripts*
- 📚 渐进式信息披露设计 / *Progressive disclosure design patterns*

---

## 🔗 相关链接 Links

- **仓库** / *Repository*: https://github.com/Y1fe1-Yang/resume-assistant-skill
- **最新版本** / *Latest Release*: https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest
- **Claude Code**: https://claude.ai/code
- **问题反馈** / *Issues*: https://github.com/Y1fe1-Yang/resume-assistant-skill/issues

---

## 📊 版本信息 Version Info

- **当前版本** / *Current Version*: 2.1.0
- **质量评分** / *Quality Score*: A (9.3/10)
- **最后更新** / *Last Updated*: 2026-02-01

---

## 🌟 特色亮点 Highlights

✨ **中文优化** - 专为中国求职市场设计
✨ **五大代理** - 覆盖求职全流程
✨ **多种格式** - PDF/DOCX/HTML/Excel 一应俱全
✨ **智能匹配** - 根据 JD 自动优化关键词
✨ **实战演练** - 模拟真实面试场景
✨ **持续成长** - 制定可执行的提升计划

---

**为 Claude Code 量身打造** | **Made for Claude Code**
