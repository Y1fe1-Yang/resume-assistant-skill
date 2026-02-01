# Resume Assistant Skill - 安装指南

## 快速安装

### 方法1：通过 Claude Code 安装（推荐）

1. 下载 `resume-assistant.skill` 文件
2. 将文件拖入 Claude Code 对话框
3. 等待安装完成

### 方法2：手动安装

```bash
# 复制技能文件到 Claude 技能目录
cp resume-assistant.skill ~/.claude/skills/

# 或使用绝对路径
cp /path/to/resume-assistant.skill ~/.claude/skills/
```

---

## ⚠️ 首次使用必读

**在使用简历生成功能前，必须完成环境配置，否则PDF生成会失败！**

---

## 环境配置

### 步骤1：安装 Python 依赖

Resume Assistant 需要以下 Python 包：

```bash
pip install fpdf2 python-docx openpyxl
```

**各包用途：**
- `fpdf2` - PDF 简历生成（必需）
- `python-docx` - Word 文档简历生成
- `openpyxl` - Excel 能力提升追踪表生成

### 步骤2：下载中文字体

PDF 生成需要中文字体支持，否则会报错：

```bash
# 创建字体目录
mkdir -p /tmp/fonts

# 下载 Noto Sans SC 字体（约17MB）
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**注意事项：**
- 字体文件约 17MB，首次下载需要一些时间
- 必须放在 `/tmp/fonts/` 目录下
- 文件名必须为 `NotoSansSC.ttf`

### 步骤3：验证安装

安装完成后，可以通过以下方式验证：

```bash
# 检查 Python 包
pip list | grep -E "fpdf2|python-docx|openpyxl"

# 检查字体文件
ls -lh /tmp/fonts/NotoSansSC.ttf

# 预期输出：
# -rw-r--r-- 1 user user 17M Feb  1 12:00 /tmp/fonts/NotoSansSC.ttf
```

---

## 系统要求

### 最低要求

- **Python**: 3.7+
- **Claude Code**: 最新版本
- **磁盘空间**: 至少 100MB（包含字体文件）
- **网络**: 安装时需要下载依赖包和字体

### 推荐配置

- **Python**: 3.9+
- **内存**: 4GB+
- **操作系统**:
  - macOS 10.14+
  - Ubuntu 20.04+
  - Windows 10+ (WSL2 推荐)

---

## 平台特定说明

### macOS

```bash
# 使用 Homebrew 安装 Python（如果需要）
brew install python3

# 安装依赖
pip3 install fpdf2 python-docx openpyxl

# 下载字体
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### Linux (Ubuntu/Debian)

```bash
# 确保 Python 和 pip 已安装
sudo apt update
sudo apt install python3 python3-pip

# 安装依赖
pip3 install fpdf2 python-docx openpyxl

# 下载字体
mkdir -p /tmp/fonts
wget -O /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### Windows (WSL2 推荐)

在 WSL2 中按照 Linux 说明操作。

**原生 Windows PowerShell：**

```powershell
# 安装依赖
pip install fpdf2 python-docx openpyxl

# 创建字体目录
New-Item -ItemType Directory -Force -Path C:\tmp\fonts

# 下载字体（使用浏览器下载）
# 或使用 curl (Windows 10+)
curl -L -o C:\tmp\fonts\NotoSansSC.ttf "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

**注意：** Windows 上字体路径可能需要调整脚本中的路径。

---

## 可选：虚拟环境安装（推荐）

使用虚拟环境可以避免依赖冲突：

```bash
# 创建虚拟环境
python3 -m venv ~/.claude/resume-assistant-env

# 激活虚拟环境
source ~/.claude/resume-assistant-env/bin/activate  # Linux/macOS
# 或
~/.claude/resume-assistant-env/Scripts/activate  # Windows

# 安装依赖
pip install fpdf2 python-docx openpyxl

# 使用完毕后退出
deactivate
```

---

## 离线安装

如果在无网络环境中安装：

### 1. 准备离线包

在有网络的机器上：

```bash
# 下载依赖包
pip download fpdf2 python-docx openpyxl -d ./offline-packages/

# 下载字体
curl -L -o NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### 2. 传输到目标机器

将 `offline-packages/` 文件夹和字体文件传输到目标机器。

### 3. 离线安装

```bash
# 安装依赖包
pip install --no-index --find-links=./offline-packages/ fpdf2 python-docx openpyxl

# 复制字体
mkdir -p /tmp/fonts
cp NotoSansSC.ttf /tmp/fonts/
```

---

## 更新

### 更新技能

```bash
# 下载新版本 skill 文件
# 然后重新安装

# 方法1：通过 Claude Code
# 拖入新的 resume-assistant.skill 文件

# 方法2：手动替换
cp resume-assistant.skill ~/.claude/skills/
```

### 更新依赖

```bash
# 更新 Python 包到最新版本
pip install --upgrade fpdf2 python-docx openpyxl

# 或更新到特定版本
pip install fpdf2==2.7.0 python-docx==1.1.0 openpyxl==3.1.0
```

---

## 卸载

### 完全卸载

```bash
# 1. 删除技能文件
rm ~/.claude/skills/resume-assistant.skill

# 2. 卸载 Python 依赖（可选）
pip uninstall fpdf2 python-docx openpyxl -y

# 3. 删除字体文件（可选）
rm -rf /tmp/fonts/NotoSansSC.ttf
```

### 保留配置卸载

如果只想禁用技能但保留环境：

```bash
# 仅移动技能文件（不删除）
mv ~/.claude/skills/resume-assistant.skill ~/.claude/skills/resume-assistant.skill.bak

# 需要时可以恢复
mv ~/.claude/skills/resume-assistant.skill.bak ~/.claude/skills/resume-assistant.skill
```

---

## 下一步

安装完成后：

1. 查看 [README.md](README.md) 了解功能概览
2. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 解决常见问题
3. 直接对 Claude 说 "帮我准备简历" 开始使用

---

## 技术支持

如遇到安装问题：

1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. 提交 [GitHub Issue](https://github.com/Y1fe1-Yang/resume-assistant-skill/issues)
3. 确保已按照本文档所有步骤操作

---

**最后更新**: 2026-02-01
**版本**: 2.0.3
