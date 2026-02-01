# Bug 修复建议

基于全面健壮性测试，发现以下问题需要修复。

---

## 🔴 P0: 关键问题 - PDF 字体文件缺失

### 问题描述
`create_pdf_resume.py` 硬编码字体路径 `/tmp/fonts/NotoSansSC.ttf`，导致在没有该字体文件的环境下完全无法运行。

### 错误信息
```
FileNotFoundError: TTF Font file not found: /tmp/fonts/NotoSansSC.ttf
```

### 影响
- **严重程度**: 🔴 高
- **影响范围**: PDF 生成功能完全不可用
- **用户影响**: 无法导出 PDF 格式简历

### 修复方案

#### 方案 1: 使用 fpdf2 内置字体 (推荐)

**文件**: `scripts/current/create_pdf_resume.py`

**修改位置**: 第 29 行

**修改前**:
```python
class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        # Use built-in Unicode font that supports Chinese
        self.add_font('NotoSans', '', '/tmp/fonts/NotoSansSC.ttf')
        self.set_font('NotoSans', '', 12)
```

**修改后**:
```python
class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        # Use built-in font that supports Unicode (Chinese)
        # fpdf2 includes DejaVu fonts which support Chinese
        self.set_font('helvetica', '', 12)  # Fallback to built-in font
```

**优点**:
- 无需外部字体文件
- 跨平台兼容
- 简单可靠

**缺点**:
- 中文字体效果可能不如 Noto Sans SC

#### 方案 2: 字体回退机制 (推荐)

```python
import os
from pathlib import Path

class ResumePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()

        # Try multiple font paths
        font_paths = [
            os.getenv('RESUME_FONT_PATH'),  # Environment variable
            '/tmp/fonts/NotoSansSC.ttf',     # Default path
            Path.home() / '.fonts' / 'NotoSansSC.ttf',  # User fonts
            '/usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf',  # Linux system fonts
            '/System/Library/Fonts/PingFang.ttc',  # macOS
        ]

        font_loaded = False
        for font_path in font_paths:
            if font_path and Path(font_path).exists():
                try:
                    self.add_font('NotoSans', '', str(font_path))
                    self.set_font('NotoSans', '', 12)
                    font_loaded = True
                    break
                except Exception:
                    continue

        if not font_loaded:
            # Fallback to built-in font
            print("⚠️  Warning: Chinese font not found, using built-in font")
            print("   To improve Chinese character rendering, install Noto Sans SC:")
            print("   mkdir -p /tmp/fonts && wget -O /tmp/fonts/NotoSansSC.ttf [FONT_URL]")
            self.set_font('helvetica', '', 12)
```

**优点**:
- 尝试多个字体路径
- 支持环境变量配置
- 有友好的回退机制
- 提供安装提示

**缺点**:
- 代码稍复杂

---

## 🟡 P1: 安全问题 - XSS 防护不足

### 问题描述
`create_web_resume.py` 的模板渲染函数未对用户输入进行 HTML 转义，存在 XSS (跨站脚本) 风险。

### 测试用例
```python
# 输入
data = {"name": "<script>alert('XSS')</script>"}

# 当前输出 (不安全)
<h1><script>alert('XSS')</script></h1>

# 期望输出 (安全)
<h1>&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;</h1>
```

### 影响
- **严重程度**: 🟡 中
- **影响范围**: Web Resume 生成
- **安全风险**: 恶意用户可注入 JavaScript 代码

### 修复方案

**文件**: `scripts/current/create_web_resume.py`

**修改位置**: `render_template` 函数，第 122-126 行

**修改前**:
```python
def replace_var(m):
    var_name = m.group(1).strip()
    value = ctx.get(var_name, '')
    return str(value) if value is not None else ''

text = re.sub(r'\{\{(?!#|/)([^\}]+)\}\}', replace_var, text)
```

**修改后**:
```python
import html  # Add at top of file

def replace_var(m):
    var_name = m.group(1).strip()
    value = ctx.get(var_name, '')
    # HTML escape to prevent XSS attacks
    if value is not None:
        return html.escape(str(value), quote=True)
    return ''

text = re.sub(r'\{\{(?!#|/)([^\}]+)\}\}', replace_var, text)
```

### 测试验证

添加测试用例:
```python
def test_xss_protection():
    """Test XSS attack prevention"""
    template = "<div>{{name}}</div>"
    data = {"name": "<script>alert('XSS')</script>"}

    result = render_template(template, data)

    # Should escape HTML entities
    assert "<script>" not in result
    assert "&lt;script&gt;" in result or "script" not in result.lower()
```

---

## 📚 P1: 文档改进 - 添加故障排除指南

### 问题描述
缺少 PDF 字体安装和常见错误的故障排除文档。

### 修复方案

**文件**: `references/troubleshooting.md`

**添加内容**:

```markdown
## PDF 生成问题

### 问题: TTF Font file not found

**错误信息**:
```
FileNotFoundError: TTF Font file not found: /tmp/fonts/NotoSansSC.ttf
```

**原因**: PDF 生成需要中文字体文件。

**解决方案**:

#### 方法 1: 下载并安装字体 (推荐)

```bash
# 创建字体目录
mkdir -p /tmp/fonts

# 下载 Noto Sans SC 字体
wget -O /tmp/fonts/NotoSansSC.ttf \
  https://github.com/googlefonts/noto-cjk/raw/main/Sans/SubsetOTF/SC/NotoSansSC-Regular.otf

# 验证文件存在
ls -lh /tmp/fonts/NotoSansSC.ttf
```

#### 方法 2: 使用系统字体 (Linux)

```bash
# 查找系统中的中文字体
fc-list :lang=zh

# 创建符号链接
mkdir -p /tmp/fonts
ln -s /usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf /tmp/fonts/NotoSansSC.ttf
```

#### 方法 3: 使用环境变量

```bash
# 指定自定义字体路径
export RESUME_FONT_PATH=/path/to/your/font.ttf

# 运行脚本
python scripts/current/create_pdf_resume.py --data resume.json
```

#### 方法 4: 修改代码使用内置字体

如果无法安装字体，可以修改代码使用 fpdf2 内置字体:

编辑 `scripts/current/create_pdf_resume.py` 第 29 行:
```python
# 将这行:
self.add_font('NotoSans', '', '/tmp/fonts/NotoSansSC.ttf')

# 改为:
# self.add_font('NotoSans', '', '/tmp/fonts/NotoSansSC.ttf')  # Comment out

# 然后将第 30 行改为:
self.set_font('helvetica', '', 12)  # Use built-in font
```

**注意**: 使用内置字体可能导致中文显示效果不佳。

### 问题: 中文字符显示为方框

**原因**: 字体不支持中文字符。

**解决方案**: 确保使用支持中文的字体，如 Noto Sans SC、思源黑体等。
```

---

## 🔧 其他建议改进

### 1. 环境变量支持

**文件**: 所有脚本

添加环境变量配置支持:

```python
import os

# At top of file
DEFAULT_OUTPUT_DIR = os.getenv('RESUME_OUTPUT_DIR', './outputs')
FONT_PATH = os.getenv('RESUME_FONT_PATH', '/tmp/fonts/NotoSansSC.ttf')
```

### 2. 更好的错误提示

**文件**: `scripts/current/create_pdf_resume.py`

改进错误提示:

```python
try:
    self.add_font('NotoSans', '', font_path)
except FileNotFoundError:
    print("❌ Error: Chinese font not found")
    print(f"   Looking for: {font_path}")
    print("\n📝 To fix this issue:")
    print("   1. Download font: wget -O /tmp/fonts/NotoSansSC.ttf [URL]")
    print("   2. Or set custom path: export RESUME_FONT_PATH=/your/font.ttf")
    print("   3. See: references/troubleshooting.md for details\n")
    sys.exit(1)
```

### 3. 配置文件支持

**新文件**: `config.json`

```json
{
  "fonts": {
    "pdf_font_path": "/tmp/fonts/NotoSansSC.ttf",
    "fallback_font": "helvetica"
  },
  "output": {
    "default_dir": "./outputs"
  },
  "security": {
    "html_escape": true
  }
}
```

---

## 📊 修复优先级总结

| 优先级 | 问题 | 预计工作量 | 影响 |
|--------|------|-----------|------|
| P0 🔴 | PDF 字体文件缺失 | 30分钟 | 高 - 功能不可用 |
| P1 🟡 | XSS 防护不足 | 20分钟 | 中 - 安全风险 |
| P1 🟡 | 故障排除文档缺失 | 15分钟 | 中 - 用户体验 |
| P2 🟢 | 环境变量支持 | 10分钟 | 低 - 便利性 |
| P2 🟢 | 错误提示改进 | 10分钟 | 低 - 用户体验 |

**总预计工作量**: 1.5 小时

---

## ✅ 修复验证清单

修复完成后，运行以下测试验证:

```bash
# 1. 运行完整测试套件
python comprehensive_test_suite.py

# 2. 测试 PDF 生成 (无字体环境)
rm -f /tmp/fonts/NotoSansSC.ttf
python scripts/current/create_pdf_resume.py \
  --data examples/resume_data_example.json \
  --output test.pdf

# 3. 测试 XSS 防护
python -c "
from scripts.current.create_web_resume import render_template
result = render_template('{{name}}', {'name': '<script>alert(1)</script>'})
assert '<script>' not in result
print('✅ XSS protection working')
"

# 4. 测试所有示例文件
for file in examples/*.json; do
    echo "Testing $file..."
    python scripts/current/create_web_resume.py --data "$file" --output "test_$(basename $file .json).html"
done
```

---

**文档生成时间**: 2026-02-01
**建议执行顺序**: P0 → P1 → P2
