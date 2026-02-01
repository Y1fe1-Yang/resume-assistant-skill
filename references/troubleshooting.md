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

### 1. PDF生成失败："Not a TrueType font"

**原因**：字体文件缺失或格式不正确

**解决方案**：
```bash
# 重新下载字体
rm -f /tmp/fonts/NotoSansSC.ttf
mkdir -p /tmp/fonts
curl -L -o /tmp/fonts/NotoSansSC.ttf \
  "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/Subset/NotoSansSC-VF.ttf"
```

### 2. 脚本找不到："No such file or directory"

**原因**：未切换到skill目录

**解决方案**：
```bash
cd ~/.claude/skills/resume-assistant
```

### 3. JSON格式错误

**原因**：JSON文件格式不正确

**解决方案**：
- 使用JSON验证工具检查语法
- 参考 `examples/resume_data_example.json` 示例文件
- 检查是否有缺失的逗号、括号、引号

### 4. 依赖包缺失

**原因**：未安装所需的Python包

**解决方案**：
```bash
pip install fpdf2 python-docx openpyxl
```

### 5. 脚本执行权限问题

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
