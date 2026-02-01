# Release Notes - v0.2.0

## 📅 发布日期
2026-02-01

## 🎉 重大更新

这是简历助手的第二个主要版本，带来了完整的多格式支持和智能用户状态检测功能。

### 核心改进

#### 1. 完美的PDF中文支持 ✅
- **问题**：v0.1.0版本使用reportlab库生成PDF时，中文显示为方块或空白
- **解决方案**：切换到fpdf2库，自动嵌入Noto Sans SC字体
- **效果**：所有中文字符完美渲染，支持复杂排版

**技术细节**：
```python
# 旧方案 (reportlab - 有问题)
from reportlab.pdfgen import canvas
canvas.drawString(x, y, "中文")  # 显示为方块

# 新方案 (fpdf2 - 完美)
from fpdf import FPDF
pdf = FPDF()
pdf.add_font('NotoSans', '', '/tmp/fonts/NotoSansSC.ttf')
pdf.set_font('NotoSans', '', 12)
pdf.cell(0, 10, "中文", ln=True)  # 完美显示
```

#### 2. 新增DOCX格式支持 📄
- 基于python-docx库实现
- 支持粗体、颜色、字体大小等专业格式
- 完全兼容Microsoft Word和WPS
- 可编辑，方便后续调整

**使用方法**：
```bash
python scripts/create_docx_resume.py output.docx --data resume_data.json
```

#### 3. 智能用户状态检测 🎯
- 通过`is_fresh_graduate`字段识别应届生/在职人员
- 自动调整简历章节顺序
- 三种格式（HTML、PDF、DOCX）均支持

**简历结构对比**：

| 用户类型 | 章节顺序 |
|---------|---------|
| 应届生 | 教育背景 → 工作经历 → 项目经验 |
| 在职人员 | 工作经历 → 项目经验 → 教育背景 |

#### 4. HTML打印优化 🖨️
- 使用`print-color-adjust: exact`保持颜色
- A4规格优化，精确控制页边距
- 所见即所得（WYSIWYG）打印效果

## 📊 性能提升

| 指标 | v0.1.0 | v0.2.0 | 提升 |
|-----|--------|--------|------|
| PDF生成速度 | N/A | 0.2秒 | 新功能 |
| 中文支持 | ❌ | ✅ | 完美 |
| 格式数量 | 1 | 3 | +200% |

## 🔧 技术栈更新

### 新增依赖
```bash
fpdf2>=2.8.1        # PDF生成
python-docx>=1.1.0  # DOCX生成
```

### 移除依赖
```bash
reportlab  # 已弃用，由fpdf2替代
```

### 安装方法
```bash
# 卸载旧依赖
pip uninstall reportlab

# 安装新依赖
pip install fpdf2>=2.8.1 python-docx>=1.1.0
```

## 📁 新增文件

### 文档
- `README.md` - 完整的使用文档
- `CHANGELOG.md` - 版本更新日志
- `RELEASE_NOTES_v0.2.0.md` - 本文档
- `examples/USAGE_GUIDE.md` - 详细使用指南

### 示例
- `examples/fresh_graduate_example.json` - 应届生简历示例
- `examples/experienced_example.json` - 在职人员简历示例

### 脚本
- `scripts/create_docx_resume.py` - DOCX生成脚本（新增）
- `scripts/create_pdf_resume.py` - PDF生成脚本（重写）
- `scripts/create_pdf_resume_reportlab.py` - 旧版备份

## 🐛 修复的问题

1. **修复PDF中文乱码** (#issue-001)
   - 问题：reportlab无法正确加载中文字体
   - 解决：切换到fpdf2库

2. **修复HTML打印颜色丢失** (#issue-002)
   - 问题：打印时蓝色标题变成黑色
   - 解决：添加print-color-adjust CSS属性

3. **修复DOCX日期对齐** (#issue-003)
   - 问题：日期无法靠右对齐
   - 解决：使用制表符实现左右对齐

## 📖 迁移指南

### 从v0.1.0升级到v0.2.0

#### 步骤1：更新依赖
```bash
pip uninstall reportlab
pip install fpdf2>=2.8.1 python-docx>=1.1.0
```

#### 步骤2：更新数据文件（可选）
在你的`resume_data.json`中添加用户状态字段：
```json
{
  "is_fresh_graduate": true,  // 应届生：true，在职：false
  "name": "张三",
  // ... 其他字段
}
```

#### 步骤3：更新脚本调用
```bash
# 旧版（已弃用）
python scripts/create_pdf_resume_reportlab.py resume.html resume.pdf

# 新版
python scripts/create_pdf_resume.py --data resume_data.json --output resume.pdf
```

### 向后兼容性
- ✅ 未设置`is_fresh_graduate`时默认为`false`（在职模式）
- ✅ 所有v0.1.0的数据文件仍然可用
- ✅ HTML模板保持兼容

## 🎯 使用示例

### 基础用法

```bash
# 生成HTML简历
python scripts/create_web_resume.py \
    --data examples/fresh_graduate_example.json \
    --template web-resume-modern \
    --output resume.html

# 生成PDF简历
python scripts/create_pdf_resume.py \
    --data examples/fresh_graduate_example.json \
    --output resume.pdf

# 生成DOCX简历
python scripts/create_docx_resume.py resume.docx \
    --data examples/fresh_graduate_example.json
```

### 批量生成

```bash
# 一次生成所有格式
for format in html pdf docx; do
    python scripts/create_${format}_resume.py \
        --data resume_data.json \
        --output resume.${format}
done
```

## 🔮 未来计划

### v0.3.0（计划中）
- [ ] 支持更多简历模板（简约、技术、设计等）
- [ ] 添加简历评分功能
- [ ] 支持模板预览

### v0.4.0（计划中）
- [ ] 集成ATS关键词优化
- [ ] 支持简历对比和版本管理
- [ ] 添加简历导入功能（从LinkedIn、智联等）

### v1.0.0（远期目标）
- [ ] Web界面和在线编辑
- [ ] 支持多语言（英文、日文等）
- [ ] AI智能简历优化建议

## 🙏 致谢

感谢以下开源项目：
- **fpdf2** - 提供优秀的PDF生成能力和中文支持
- **python-docx** - 强大的DOCX文档处理库
- **Noto Sans SC** - Google开源的高质量中文字体

感谢社区反馈和建议，让这个版本更加完善！

## 📮 反馈渠道

- **GitHub Issues**: [报告问题](https://github.com/yourusername/resume-assistant/issues)
- **GitHub Discussions**: [功能建议](https://github.com/yourusername/resume-assistant/discussions)
- **Email**: your.email@example.com

## 📄 完整更新日志

详细的更新日志请查看 [CHANGELOG.md](CHANGELOG.md)

---

**简历助手v0.2.0 - 让每个人都能拥有一份出色的简历！** 🚀
