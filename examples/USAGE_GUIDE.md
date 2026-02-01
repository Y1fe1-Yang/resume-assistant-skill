# 使用指南

本文档提供详细的使用示例和最佳实践。

## 📂 示例文件

| 文件 | 说明 | 适用场景 |
|------|------|---------|
| `fresh_graduate_example.json` | 应届生简历示例 | 在校生、应届毕业生 |
| `experienced_example.json` | 在职人员简历示例 | 有工作经验的求职者 |

## 🚀 快速开始

### 示例1：生成应届生简历（所有格式）

```bash
cd /path/to/resume-assistant

# 1. 生成HTML简历
python scripts/create_web_resume.py \
    --data examples/fresh_graduate_example.json \
    --template web-resume-modern \
    --output examples/output/fresh_graduate.html

# 2. 生成PDF简历
python scripts/create_pdf_resume.py \
    --data examples/fresh_graduate_example.json \
    --output examples/output/fresh_graduate.pdf

# 3. 生成DOCX简历
python scripts/create_docx_resume.py examples/output/fresh_graduate.docx \
    --data examples/fresh_graduate_example.json
```

**预期结果**：
- HTML：现代化网页简历，教育背景在前
- PDF：专业排版，中文完美显示
- DOCX：可编辑Word文档

### 示例2：生成在职人员简历

```bash
cd /path/to/resume-assistant

# 生成PDF简历（推荐用于投递）
python scripts/create_pdf_resume.py \
    --data examples/experienced_example.json \
    --output examples/output/experienced.pdf
```

**预期结果**：
- 工作经历在前，突出5年互联网经验
- 项目经验展示个人项目和开源贡献
- 教育背景靠后，淡化学历

## 📊 格式对比

### HTML格式特点

**优势**：
- ✅ 预览方便，直接在浏览器打开
- ✅ 可以使用浏览器打印功能生成PDF
- ✅ 颜色和排版完全一致

**适用场景**：
- 本地预览和快速迭代
- 打印纸质简历
- 个人网站展示

**示例**：
```bash
# 生成HTML并在浏览器中打开
python scripts/create_web_resume.py \
    --data examples/fresh_graduate_example.json \
    --template web-resume-modern \
    --output resume.html

# Linux/Mac
open resume.html

# Windows
start resume.html
```

**打印技巧**：
1. 在浏览器中打开HTML文件
2. 按 `Ctrl+P` (Windows) 或 `Cmd+P` (Mac)
3. 设置：
   - 纸张大小：A4
   - 边距：默认
   - 背景图形：✅ 启用（重要！）
4. 保存为PDF或直接打印

### PDF格式特点

**优势**：
- ✅ 通用性最强，所有设备都能打开
- ✅ 格式固定，不会因软件版本而变化
- ✅ 适合在线投递和邮件发送

**适用场景**：
- 在线招聘平台投递
- 邮件发送给HR
- 打印纸质简历

**示例**：
```bash
python scripts/create_pdf_resume.py \
    --data examples/experienced_example.json \
    --output resume.pdf
```

**验证方法**：
```bash
# 检查PDF文件大小（正常应该在50-100KB）
ls -lh resume.pdf

# 在PDF阅读器中打开，检查：
# 1. 中文是否正常显示
# 2. 颜色是否保留（蓝色标题）
# 3. 排版是否整齐
```

### DOCX格式特点

**优势**：
- ✅ 可编辑，方便后续调整
- ✅ Word兼容性好
- ✅ 支持导出为PDF

**适用场景**：
- 需要频繁修改内容
- HR要求提供Word格式
- 作为备份格式

**示例**：
```bash
python scripts/create_docx_resume.py resume.docx \
    --data examples/fresh_graduate_example.json
```

**编辑建议**：
1. 使用Microsoft Word或WPS打开
2. 保持原有格式（字体、颜色、间距）
3. 修改后另存为PDF投递

## 🎯 最佳实践

### 1. 根据岗位定制简历

**场景**：投递不同岗位需要调整简历重点

**方法**：
```bash
# 1. 复制基础数据
cp examples/fresh_graduate_example.json my_resume_base.json

# 2. 针对产品工程师岗位
cp my_resume_base.json my_resume_product_engineer.json
# 编辑 my_resume_product_engineer.json：
# - 调整项目顺序，相关项目放前面
# - 修改"其他"部分，强调产品思维

# 3. 针对软件工程师岗位
cp my_resume_base.json my_resume_software_engineer.json
# 编辑 my_resume_software_engineer.json：
# - 突出编程项目
# - 强调技术能力

# 4. 分别生成
python scripts/create_pdf_resume.py \
    --data my_resume_product_engineer.json \
    --output resume_product_engineer.pdf

python scripts/create_pdf_resume.py \
    --data my_resume_software_engineer.json \
    --output resume_software_engineer.pdf
```

### 2. 版本管理

**场景**：跟踪简历修改历史

**方法**：
```bash
# 使用git管理简历数据
git init
git add examples/*.json
git commit -m "Initial resume version"

# 每次修改后提交
git add my_resume.json
git commit -m "Update: highlight algorithm optimization project"

# 查看修改历史
git log --oneline

# 回退到之前版本
git checkout <commit-id> my_resume.json
```

### 3. 批量生成

**场景**：一次生成所有格式

**方法**：
```bash
#!/bin/bash
# save as: generate_all.sh

DATA_FILE="$1"
OUTPUT_PREFIX="${DATA_FILE%.json}"

echo "Generating all formats for $DATA_FILE..."

# HTML
python scripts/create_web_resume.py \
    --data "$DATA_FILE" \
    --template web-resume-modern \
    --output "${OUTPUT_PREFIX}.html"

# PDF
python scripts/create_pdf_resume.py \
    --data "$DATA_FILE" \
    --output "${OUTPUT_PREFIX}.pdf"

# DOCX
python scripts/create_docx_resume.py "${OUTPUT_PREFIX}.docx" \
    --data "$DATA_FILE"

echo "Done! Generated:"
echo "  - ${OUTPUT_PREFIX}.html"
echo "  - ${OUTPUT_PREFIX}.pdf"
echo "  - ${OUTPUT_PREFIX}.docx"
```

使用：
```bash
chmod +x generate_all.sh
./generate_all.sh examples/fresh_graduate_example.json
```

### 4. 数据验证

**场景**：确保数据格式正确

**方法**：
```python
# validate_resume_data.py
import json
import sys

def validate_resume(data):
    """验证简历数据完整性"""
    errors = []

    # 必填字段
    required = ['name']
    for field in required:
        if not data.get(field):
            errors.append(f"Missing required field: {field}")

    # 推荐字段
    recommended = ['summary', 'experience', 'education', 'skills']
    for field in recommended:
        if not data.get(field):
            print(f"Warning: Missing recommended field: {field}")

    # 检查数组字段
    if data.get('experience'):
        for i, exp in enumerate(data['experience']):
            if not exp.get('company'):
                errors.append(f"Experience[{i}]: missing company")

    return errors

# 使用
if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = json.load(f)

    errors = validate_resume(data)
    if errors:
        print("Validation errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Resume data is valid!")
```

## 🐛 常见问题

### Q1: PDF生成很慢

**原因**：首次运行需要下载字体文件

**解决**：
```bash
# 预先下载字体
mkdir -p /tmp/fonts
wget -O /tmp/fonts/NotoSansSC.ttf \
    "https://github.com/notofonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.ttf"
```

### Q2: HTML打印时颜色消失

**原因**：浏览器默认不打印背景色

**解决**：
1. Chrome/Edge：打印对话框 → 更多设置 → ✅ 背景图形
2. Firefox：页面设置 → ✅ 打印背景色和背景图像
3. Safari：打印对话框 → ✅ 打印背景

### Q3: DOCX在手机上格式错乱

**原因**：手机Office版本兼容性问题

**解决**：
```bash
# 将DOCX转为PDF再发送
# 方法1: 使用Word导出
# 方法2: 直接生成PDF格式
python scripts/create_pdf_resume.py --data resume_data.json --output resume.pdf
```

### Q4: 如何修改模板样式

**场景**：想要不同的颜色或字体

**方法**：
```bash
# 1. 复制模板
cp assets/templates/web-resume-modern.html \
   assets/templates/my-custom-template.html

# 2. 编辑CSS部分
# 修改颜色：找到 #2563eb（蓝色），替换为你喜欢的颜色
# 修改字体：找到 font-family，修改字体名称

# 3. 使用自定义模板
python scripts/create_web_resume.py \
    --data resume_data.json \
    --template my-custom-template \
    --output resume.html
```

## 📈 进阶技巧

### 自动化工作流

使用GitHub Actions自动生成简历：

```yaml
# .github/workflows/generate-resume.yml
name: Generate Resume

on:
  push:
    paths:
      - 'resume_data.json'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install fpdf2 python-docx

      - name: Generate resumes
        run: |
          python scripts/create_pdf_resume.py \
            --data resume_data.json \
            --output resume.pdf

      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: resume
          path: resume.pdf
```

## 🎓 学习资源

- **简历写作指南**：`references/writing-guide.md`
- **行业关键词**：`references/industry-keywords.md`
- **五大代理详细说明**：`references/agent-*.md`

---

**有问题？** 查看 [GitHub Issues](https://github.com/yourusername/resume-assistant/issues) 或参考 README.md
