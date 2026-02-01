# 字体文件说明

## Noto Sans SC (思源黑体简体中文)

本目录包含 PDF 简历生成所需的中文字体文件。

### 文件信息

- **文件名**: `NotoSansSC.ttf`
- **字体**: Noto Sans SC Variable Font (可变字体)
- **大小**: 约 17MB
- **来源**: Google Noto CJK 项目
- **许可**: SIL Open Font License 1.1

### 使用说明

此字体文件已集成在 skill 中，PDF 生成脚本会自动使用：

```python
# scripts/current/create_pdf_resume.py 会自动查找此字体
# 优先级顺序:
# 1. assets/fonts/NotoSansSC.ttf (本文件 - 最高优先级)
# 2. $RESUME_FONT_PATH 环境变量指定的路径
# 3. /tmp/fonts/NotoSansSC.ttf
# 4. ~/.fonts/NotoSansSC.ttf
# 5. 系统字体路径
```

### 字体特性

- ✅ 完整支持简体中文
- ✅ 支持常用标点符号
- ✅ 支持英文字母和数字
- ✅ 可变字体，文件大小优化
- ✅ 适合打印和屏幕显示

### 许可证

本字体遵循 SIL Open Font License 1.1，允许自由使用、修改和分发。

详见: https://github.com/googlefonts/noto-cjk

### 更新字体

如需更新到最新版本：

```bash
curl -L -o assets/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```
