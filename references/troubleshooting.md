# 故障排查指南

## 环境配置

### 首次使用必需配置

在使用脚本生成简历文件前，必须完成以下配置：

```bash
# 1. 安装Python依赖
pip install fpdf2 python-docx openpyxl

# 2. 下载中文字体（PDF生成必需）
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**注意**：字体文件约17MB，首次下载需要一些时间。

---

## 常见问题

### 1. PDF生成失败："TTF Font file not found"

**错误信息**：
```
FileNotFoundError: TTF Font file not found: /tmp/fonts/NotoSansSC.ttf
```

**原因**：中文字体文件未安装

**解决方案**：

#### 方法 1: 下载字体到默认路径（推荐）
```bash
# 创建字体目录
mkdir -p /tmp/fonts

# 下载 Noto Sans SC 字体
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"

# 验证文件存在
ls -lh /tmp/fonts/NotoSansSC.ttf
```

#### 方法 2: 使用系统字体 (Linux)
```bash
# 查找系统中的中文字体
fc-list :lang=zh

# 创建符号链接到系统字体
mkdir -p /tmp/fonts
ln -s /usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf /tmp/fonts/NotoSansSC.ttf
```

#### 方法 3: 使用自定义字体路径
```bash
# 设置环境变量指定字体路径
export RESUME_FONT_PATH=/path/to/your/font.ttf

# 运行脚本
python scripts/current/create_pdf_resume.py --data resume.json
```

#### 方法 4: 使用内置字体（中文显示可能不佳）
如果无法安装字体，脚本会自动回退到内置的 helvetica 字体。虽然可以生成 PDF，但中文字符显示效果可能不理想。脚本会显示警告信息并继续执行。

**注意**：
- 字体文件约 17MB，首次下载需要一些时间
- 使用内置字体不需要下载，但中文显示效果不佳
- 推荐使用方法 1 以获得最佳中文显示效果

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
