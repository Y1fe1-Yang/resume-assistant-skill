# Resume Assistant Skill v2.0.3

## 🎯 本次更新

专注于 **DOCX 简历字体统一性优化**，彻底解决字体大小不一致问题，让生成的简历更加整齐专业。

## ✨ 主要改进

### DOCX 字体完全统一

完全重写 `create_docx_resume.py`，统一字体大小体系：

- **姓名**: 16pt
- **章节标题**: 14pt（教育背景、工作经历等）
- **副标题**: 11pt（公司名、项目名、学校名）
- **正文**: 10.5pt（所有正文内容）
- **辅助信息**: 9pt（日期、联系方式）

### 技术改进

- ✅ 引入字体大小常量统一管理
- ✅ 使用 `qn('w:eastAsia')` 显式设置中文字体（微软雅黑）
- ✅ 移除 Word 样式依赖，避免样式冲突
- ✅ 使用 Unicode 子弹符号（•）替代样式列表
- ✅ 代码重构，提升可读性和可维护性

## 📊 测试结果

```
✅ 姓名: 16.0pt
✅ 章节标题: 14.0pt
✅ 副标题: 11.0pt
✅ 正文: 10.5pt
✅ 辅助信息: 9.0pt
✅ 文件大小: 38KB
✅ 视觉效果: 整齐统一，专业度显著提升
```

## 🔧 修改文件

- `scripts/create_docx_resume.py` - 完全重写（398行）

## 🚀 升级指南

### 从 v2.0.2 升级

```bash
cd ~/.claude/skills/resume-assistant-skill
git pull origin main
cat VERSION  # 应显示: v2.0.3
```

### 兼容性

- ✅ **完全向后兼容** - 无需修改 JSON 数据文件
- ✅ **无破坏性变更** - 现有脚本和工作流完全不受影响
- ✅ **即插即用** - 升级后立即生效

## 📝 完整变更日志

查看 [CHANGELOG.md](./CHANGELOG.md)

## 🙏 致谢

感谢 @Y1fe1-Yang 发现并报告字体不一致问题。

---

**Full Changelog**: https://github.com/Y1fe1-Yang/resume-assistant-skill/compare/v2.0.2...v2.0.3
