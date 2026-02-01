# Resume Assistant Skill - 故障排查指南

## 目录

1. [PDF 生成问题](#pdf-生成问题)
2. [脚本执行问题](#脚本执行问题)
3. [依赖包问题](#依赖包问题)
4. [字体问题](#字体问题)
5. [数据格式问题](#数据格式问题)
6. [技能加载问题](#技能加载问题)
7. [常见错误代码](#常见错误代码)

---

## PDF 生成问题

### 错误1：`Not a TrueType font`

**症状：**
```
FPDFException: Not a TrueType font: /tmp/fonts/NotoSansSC.ttf
```

**原因：** 字体文件缺失或损坏

**解决方案：**

```bash
# 1. 删除旧字体（如果存在）
rm -f /tmp/fonts/NotoSansSC.ttf

# 2. 创建目录
mkdir -p /tmp/fonts

# 3. 重新下载字体
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"

# 4. 验证字体文件
ls -lh /tmp/fonts/NotoSansSC.ttf
# 应该显示约 17MB 的文件
```

**Windows 用户：**
```powershell
# 删除旧字体
Remove-Item C:\tmp\fonts\NotoSansSC.ttf -ErrorAction SilentlyContinue

# 创建目录
New-Item -ItemType Directory -Force -Path C:\tmp\fonts

# 下载字体
Invoke-WebRequest -Uri "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf" -OutFile C:\tmp\fonts\NotoSansSC.ttf
```

### 错误2：`ModuleNotFoundError: No module named 'fpdf'`

**症状：**
```
ModuleNotFoundError: No module named 'fpdf'
```

**原因：** 未安装 fpdf2 包

**解决方案：**

```bash
# 安装 fpdf2（注意是 fpdf2 不是 fpdf）
pip install fpdf2

# 如果已安装旧版 fpdf，先卸载
pip uninstall fpdf -y
pip install fpdf2
```

### 错误3：PDF 生成但中文显示为乱码

**原因：** 字体未正确加载或使用了错误的字体

**解决方案：**

1. 确保字体路径正确：
```bash
# 检查字体是否存在
ls -lh /tmp/fonts/NotoSansSC.ttf
```

2. 检查脚本中的字体路径：
```python
# 应该是：
pdf.add_font('NotoSansSC', '', '/tmp/fonts/NotoSansSC.ttf', uni=True)
```

---

## 脚本执行问题

### 错误4：`No such file or directory`

**症状：**
```
python: can't open file 'create_pdf_resume.py': [Errno 2] No such file or directory
```

**原因：** 未在正确的目录中运行脚本

**解决方案：**

```bash
# 方法1：切换到脚本目录
cd ~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant/scripts/current
python create_pdf_resume.py --data resume_data.json --output resume.pdf

# 方法2：使用绝对路径
python ~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant/scripts/current/create_pdf_resume.py \
  --data ~/resume_data.json \
  --output ~/resume.pdf
```

### 错误5：`FileNotFoundError: [Errno 2] No such file or directory: 'resume_data.json'`

**原因：** 数据文件路径不正确

**解决方案：**

```bash
# 检查数据文件位置
ls -la resume_data.json

# 使用绝对路径
python create_pdf_resume.py \
  --data /full/path/to/resume_data.json \
  --output /full/path/to/resume.pdf
```

### 错误6：权限不足

**症状：**
```
PermissionError: [Errno 13] Permission denied: 'resume.pdf'
```

**解决方案：**

```bash
# 检查目标目录权限
ls -ld .

# 更改输出目录
python create_pdf_resume.py --data resume_data.json --output ~/Documents/resume.pdf

# 或给予写入权限
chmod u+w .
```

---

## 依赖包问题

### 错误7：pip 安装失败

**症状：**
```
ERROR: Could not install packages due to an OSError
```

**解决方案：**

```bash
# 方法1：使用用户安装（推荐）
pip install --user fpdf2 python-docx openpyxl

# 方法2：升级 pip
pip install --upgrade pip
pip install fpdf2 python-docx openpyxl

# 方法3：使用 sudo（不推荐）
sudo pip install fpdf2 python-docx openpyxl
```

### 错误8：版本冲突

**症状：**
```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed
```

**解决方案：**

```bash
# 创建虚拟环境（推荐）
python3 -m venv resume-env
source resume-env/bin/activate  # Linux/macOS
# 或
resume-env\Scripts\activate  # Windows

# 在虚拟环境中安装
pip install fpdf2 python-docx openpyxl
```

### 错误9：`command not found: pip`

**原因：** pip 未安装或不在 PATH 中

**解决方案：**

```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip

# 验证安装
pip3 --version
```

---

## 字体问题

### 错误10：字体下载超时

**症状：**
```
curl: (28) Operation timed out after 300000 milliseconds
```

**解决方案：**

```bash
# 方法1：使用镜像源（中国大陆用户）
# 手动从以下地址下载字体：
# https://ghproxy.com/https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf

# 方法2：增加超时时间
curl -L --max-time 600 -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"

# 方法3：使用 wget
wget -O /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### 错误11：字体文件大小不对

**症状：** 字体文件下载完成但只有几KB

**原因：** 下载不完整或下载到了错误页面

**解决方案：**

```bash
# 检查文件大小（应该约17MB）
ls -lh /tmp/fonts/NotoSansSC.ttf

# 如果不对，删除并重新下载
rm /tmp/fonts/NotoSansSC.ttf

# 使用浏览器手动下载，然后移动到正确位置
mv ~/Downloads/NotoSansSC-VF.ttf /tmp/fonts/NotoSansSC.ttf
```

---

## 数据格式问题

### 错误12：JSON 解析错误

**症状：**
```
JSONDecodeError: Expecting property name enclosed in double quotes
```

**原因：** JSON 格式不正确

**解决方案：**

1. 使用 JSON 验证工具检查格式
2. 确保使用双引号而非单引号
3. 检查是否有多余的逗号
4. 参考示例文件：

```bash
# 查看示例文件
cat ~/.claude/skills/resume-assistant-skill/resume-assistant-source/resume-assistant/examples/resume_data_example.json
```

### 错误13：必填字段缺失

**症状：**
```
KeyError: 'name'
```

**原因：** JSON 数据缺少必填字段

**解决方案：**

确保 JSON 包含至少以下字段：

```json
{
  "name": "姓名",
  "title": "求职意向",
  "phone": "联系电话",
  "email": "邮箱地址"
}
```

完整格式参考 `examples/resume_data_example.json`

### 错误14：数据类型错误

**症状：**
```
TypeError: 'NoneType' object is not iterable
```

**原因：** 某些字段应该是列表但提供了 null

**解决方案：**

```json
// 错误：
{
  "education": null
}

// 正确：
{
  "education": []
}
```

---

## 技能加载问题

### 错误15：Claude 无法识别技能

**症状：** 对 Claude 说触发词但没有响应

**原因：** 技能文件未正确安装

**解决方案：**

```bash
# 检查技能文件是否存在
ls -la ~/.claude/skills/ | grep resume

# 重新安装
cp resume-assistant.skill ~/.claude/skills/

# 重启 Claude Code
```

### 错误16：技能加载但功能不全

**症状：** 部分功能无法使用

**原因：** 技能文件版本不匹配

**解决方案：**

```bash
# 检查版本
cat ~/.claude/skills/resume-assistant-skill/VERSION

# 下载最新版本并重新安装
# 从 GitHub releases 页面下载
```

---

## 常见错误代码

| 错误代码 | 含义 | 快速解决方案 |
|---------|------|------------|
| Exit code 1 | 一般脚本错误 | 检查命令语法和路径 |
| Exit code 2 | 文件未找到 | 验证文件路径 |
| Exit code 127 | 命令未找到 | 确保 Python 和依赖已安装 |
| Exit code 13 | 权限拒绝 | 使用 chmod 或更改目录 |

---

## 诊断工具

### 环境检查脚本

创建并运行以下脚本以诊断环境问题：

```bash
#!/bin/bash
# check_environment.sh

echo "=== Resume Assistant Environment Check ==="
echo

echo "1. Python Version:"
python3 --version
echo

echo "2. pip Version:"
pip3 --version
echo

echo "3. Installed Packages:"
pip3 list | grep -E "fpdf2|python-docx|openpyxl"
echo

echo "4. Font File:"
if [ -f "/tmp/fonts/NotoSansSC.ttf" ]; then
    echo "✓ Font found"
    ls -lh /tmp/fonts/NotoSansSC.ttf
else
    echo "✗ Font NOT found"
fi
echo

echo "5. Skill File:"
if [ -f "$HOME/.claude/skills/resume-assistant.skill" ]; then
    echo "✓ Skill installed"
else
    echo "✗ Skill NOT installed"
fi
echo

echo "=== Check Complete ==="
```

运行：
```bash
bash check_environment.sh
```

---

## 调试模式

如果问题仍未解决，启用调试模式：

```bash
# 运行脚本时添加详细输出
python -v create_pdf_resume.py --data resume_data.json --output resume.pdf

# 或使用 Python 调试器
python -m pdb create_pdf_resume.py --data resume_data.json --output resume.pdf
```

---

## 获取帮助

如果以上方法都无法解决问题：

### 1. 收集诊断信息

```bash
# 创建诊断报告
{
  echo "=== System Information ==="
  uname -a
  echo
  echo "=== Python Version ==="
  python3 --version
  echo
  echo "=== Installed Packages ==="
  pip3 list
  echo
  echo "=== Font Status ==="
  ls -lh /tmp/fonts/
  echo
  echo "=== Error Message ==="
  # 粘贴完整错误消息
} > diagnostic_report.txt
```

### 2. 提交 Issue

1. 访问 [GitHub Issues](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues)
2. 点击 "New Issue"
3. 附上 `diagnostic_report.txt` 文件
4. 详细描述问题和复现步骤

### 3. 社区支持

- 查看 [GitHub Discussions](https://github.com/Y1fe1-Yang/resume-assistant-skill/discussions)
- 搜索类似问题
- 参与讨论

---

## 已知问题

### Issue #1: Windows 路径问题
- **状态**: 已知
- **影响**: Windows 用户可能需要调整脚本中的路径
- **临时方案**: 使用 WSL2 或修改脚本路径

### Issue #2: Python 2.x 不兼容
- **状态**: 不会修复
- **解决**: 升级到 Python 3.7+

### Issue #3: macOS Catalina 字体权限
- **状态**: 已知
- **临时方案**: 使用用户目录存放字体

---

## 预防性维护

定期执行以下检查可以避免问题：

```bash
# 每月一次
pip install --upgrade fpdf2 python-docx openpyxl

# 验证字体完整性
sha256sum /tmp/fonts/NotoSansSC.ttf

# 备份重要数据
cp resume_data.json resume_data_backup.json
```

---

**最后更新**: 2026-02-01
**版本**: 2.0.3

如果本文档未能解决您的问题，请提交 [Issue](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues) 以便我们改进文档。
