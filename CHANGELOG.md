# Changelog

All notable changes to this project will be documented in this file.

## [v2.0.3] - 2026-02-01

### Fixed
- **DOCX字体统一性问题** (P0): 完全重写DOCX生成代码，统一所有字体大小和样式
  - 姓名: 16pt
  - 章节标题: 14pt
  - 副标题（公司/项目名）: 11pt
  - 正文: 10.5pt
  - 辅助信息（日期/联系方式）: 9pt
- **中文字体渲染问题**: 使用 `qn('w:eastAsia')` 显式设置中文字体（微软雅黑），确保中文字符渲染一致
- **样式混用问题**: 移除 `style="List Bullet"` 依赖，改用手动设置字体，避免Word样式冲突

### Improved
- 引入字体大小常量（FONT_SIZE_*）统一管理
- 添加 `set_chinese_font()` 辅助函数确保字体一致性
- 所有文本元素均使用 Unicode 子弹符号（•）而非样式
- 改进代码可读性和可维护性，添加详细注释

### Technical Details
- 修改文件: create_docx_resume.py（完全重写）
- 新增功能: 显式中文字体设置、统一字体常量系统
- 向后兼容: 完全兼容，无破坏性变更
- 测试结果: ✅ 所有字体大小符合预期，视觉效果整齐统一

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
