# Changelog

All notable changes to this project will be documented in this file.

## [v2.0.2] - 2026-02-01

### Fixed
- **SKILL.md路径错误** (P0): 修复了5处错误路径,从 `~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant` 改为 `~/.claude/skills/resume-assistant-skill`
- **DOCX字体大小不一致** (P0): 统一了所有副标题字体为Pt(10),为角色和学位信息添加灰色RGB(102,102,102)
- **Excel数据结构不匹配** (P0): 重写了4个sheet生成函数,适配新的JSON格式(timeline、task字段)
- **Excel任务不够详细** (P1): 完全重写任务追踪表生成逻辑,新增智能任务分解功能(~150行代码),支持4种任务类型自动分解

### Improved
- Excel追踪表从抽象任务变为每周具体行动项,包含工时预估和明确截止日期
- DOCX简历格式更加整齐专业,视觉层次更清晰
- 所有脚本路径现在100%正确,用户可以按文档直接执行

### Technical Details
- 修改文件: SKILL.md, create_docx_resume.py, create_growth_tracker.py
- 新增代码: ~150行(任务分解逻辑)
- 向后兼容: 完全兼容,无破坏性变更

## [v2.0.1] - 2026-01-30

### Fixed
- PDF中文字体支持(从reportlab迁移到fpdf2)
- 修复了脚本路径问题

## [v2.0.0] - 2026-01-28

### Added
- 五个专业代理系统
- PDF/DOCX/HTML简历生成
- Excel能力提升追踪表
- 完整的SKILL.md文档

### Features
- 代理1: 故事挖掘代理
- 代理2: 职位推荐代理
- 代理3: 简历优化代理
- 代理4: 模拟面试代理
- 代理5: 能力提升代理
