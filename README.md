# Resume Assistant Skill

[![GitHub release](https://img.shields.io/github/v/release/Y1fe1-Yang/resume-assistant-skill)](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)
[![License](https://img.shields.io/github/license/Y1fe1-Yang/resume-assistant-skill)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Skill-7C3AED)](https://claude.ai/code)

智能简历助手 - AI-powered resume assistant with 5 specialized agents for Chinese job seekers.

一个为 [Claude Code](https://claude.ai/code) 设计的技能包，通过五个专业 AI 代理提供全流程求职支持。

---

## 📦 Installation

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

---

## ✨ Features

### Five Specialized AI Agents

- **🔍 Story Mining Agent** - Discover overlooked experiences and highlight transferable skills
- **💼 Job Recommendation Agent** - Match suitable positions based on background and interests
- **📝 Resume Optimization Agent** - Tailor content to specific job descriptions with keyword optimization
- **🎭 Mock Interview Agent** - Practice interviews with realistic questions and constructive feedback
- **📈 Growth Planning Agent** - Analyze skill gaps and create actionable development plans

### Output Formats

- 📄 **PDF** - Professional format for formal applications
- 📝 **DOCX** - Editable format for further customization
- 🌐 **HTML** - Modern responsive design with dark mode support
- 📊 **Excel** - Growth tracking spreadsheet with milestones

---

## 🚀 Quick Start

After installation, simply chat with Claude Code:

```
"帮我写简历"           # Create a resume
"优化这份简历"         # Optimize existing resume
"模拟面试"            # Practice interview
"职业规划"            # Career planning
"我想冲XX岗位但能力不够" # Skill gap analysis
```

---

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill documentation (for Claude)
- **[skillmap.json](skillmap.json)** - Skill metadata
- **[examples/](examples/)** - Sample data files
- **[Releases](https://github.com/Y1fe1-Yang/resume-assistant-skill/releases)** - Download packaged skill

---

## 🎯 Use Cases

| Scenario | Agents Used | Output |
|----------|-------------|--------|
| First-time resume | Story Mining → Resume Optimization | Polished resume |
| Job application | Resume Optimization | Tailored resume |
| Interview prep | Mock Interview | Practice feedback |
| Career development | Job Recommendation → Growth Planning | Development plan |
| Complete job search | All 5 agents | End-to-end support |

---

## 📋 Requirements

- **Claude Code** installed
- **Python 3.7+** for script execution
- **Python packages**: `fpdf2`, `python-docx`, `openpyxl`
- **Font**: NotoSansSC (for Chinese PDF generation)

---

## 📄 License

[MIT](LICENSE)

---

## 🙏 Acknowledgments

This skill provides comprehensive career assistance for Chinese job seekers through:
- AI-powered conversational guidance
- Domain expertise in resume writing
- Reliable document generation scripts
- Progressive disclosure design patterns

---

## 🔗 Links

- **Repository**: https://github.com/Y1fe1-Yang/resume-assistant-skill
- **Latest Release**: https://github.com/Y1fe1-Yang/resume-assistant-skill/releases/latest
- **Claude Code**: https://claude.ai/code

---

**Made for Claude Code** | **Version 2.1.0** | **Quality: A (9.3/10)**
