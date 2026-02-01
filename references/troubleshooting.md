# 故障排查指南

## 环境配置

### 首次使用必需配置

在使用脚本生成简历文件前，只需安装 Python 依赖：

```bash
# 安装Python依赖
pip install fpdf2 python-docx openpyxl
```

**✅ 中文字体已内置**：
- 本 skill 已包含 Noto Sans SC 中文字体（位于 `assets/fonts/NotoSansSC.ttf`）
- PDF 生成功能开箱即用，无需手动下载或配置字体
- 字体大小约 17MB，已包含在 skill 包中

---

## 常见问题

### 1. PDF生成失败："TTF Font file not found"

**错误信息**：
```
FileNotFoundError: TTF Font file not found
```

**原因**：内置字体文件丢失或 skill 安装不完整

**正常情况**：本 skill 已内置中文字体（`assets/fonts/NotoSansSC.ttf`），通常不会出现此错误。

**排查步骤**：

#### 步骤 1: 检查内置字体是否存在
```bash
# 在 skill 目录下检查
ls -lh assets/fonts/NotoSansSC.ttf

# 应该看到约 17MB 的字体文件
```

#### 步骤 2: 如果内置字体丢失，重新下载
```bash
# 下载字体到 skill 的 assets/fonts 目录
mkdir -p assets/fonts
curl -L -o assets/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

#### 步骤 3: 使用自定义字体（可选）
```bash
# 设置环境变量指定自定义字体路径
export RESUME_FONT_PATH=/path/to/your/font.ttf

# 运行脚本
python scripts/current/create_pdf_resume.py --data resume.json
```

#### 步骤 4: Fallback 模式（最后手段）
如果以上方法都失败，脚本会自动回退到内置的 helvetica 字体。虽然可以生成 PDF，但中文字符会显示为占位符。脚本会显示警告信息并继续执行。

**注意**：
- 内置字体已包含，正常情况下不需要手动配置
- 如果遇到此错误，说明 skill 安装可能不完整
- 建议重新安装 skill 或手动下载字体到 `assets/fonts/` 目录

### 2. PDF生成失败："Not a TrueType font"

**原因**：字体文件损坏或格式不正确

**解决方案**：
```bash
# 删除旧的字体文件并重新下载
rm -f /tmp/fonts/NotoSansSC.ttf
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### 3. 脚本找不到："No such file or directory"

**原因**：未切换到skill目录

**解决方案**：
```bash
cd ~/.claude/skills/resume-assistant
```

### 4. JSON格式错误

**原因**：JSON文件格式不正确

**解决方案**：
- 使用JSON验证工具检查语法
- 参考 `examples/resume_data_example.json` 示例文件
- 检查是否有缺失的逗号、括号、引号

### 5. 依赖包缺失

**原因**：未安装所需的Python包

**解决方案**：
```bash
pip install fpdf2 python-docx openpyxl
```

### 6. 脚本执行权限问题

**原因**：脚本没有执行权限

**解决方案**：
```bash
chmod +x scripts/current/*.py
```

---

## 脚本使用强制要求

当用户要求生成简历文件（PDF/DOCX/HTML）时：

1. **必须且只能**使用 `scripts/` 目录下提供的脚本
2. **严禁**自行编写类似功能的代码来替代这些脚本
3. 如果脚本执行失败，应该**解决环境问题**（如安装依赖、下载字体），而不是绕过它
4. **禁止**使用其他第三方库或工具重新实现这些功能
