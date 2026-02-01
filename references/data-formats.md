# 数据格式参考

本文档详细说明代理输出的JSON数据格式，供脚本生成最终文件使用。

---

## 简历数据格式 (resume_data.json)

代理3（简历优化代理）完成后会自动生成此格式，也可以手动创建。

### 完整示例

```json
{
  "name": "姓名",
  "title": "求职意向",
  "phone": "联系电话",
  "email": "邮箱地址",
  "location": "所在城市",
  "is_fresh_graduate": true,
  "summary": "个人简介（1-2句话）",
  "education": [
    {
      "school": "学校名称",
      "degree": "学位（本科/硕士/博士）",
      "major": "专业名称",
      "startDate": "2020.09",
      "endDate": "2024.06",
      "gpa": "3.6/4.0"
    }
  ],
  "projects": [
    {
      "name": "项目名称",
      "role": "你的角色",
      "date": "2023.06 - 2023.12",
      "tech": ["技术1", "技术2", "技术3"],
      "details": [
        "项目成果描述1（建议量化）",
        "项目成果描述2（建议量化）"
      ]
    }
  ],
  "experience": [
    {
      "company": "公司名称",
      "position": "职位名称",
      "startDate": "2023.01",
      "endDate": "2023.12",
      "achievements": [
        "工作成果描述1",
        "工作成果描述2"
      ]
    }
  ],
  "skills": [
    {
      "category": "技能分类",
      "items": "具体技能列表（逗号分隔）"
    }
  ],
  "other": [
    "其他信息（奖学金、证书等）"
  ]
}
```

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | ✅ | 姓名 |
| `title` | string | ❌ | 求职意向 |
| `phone` | string | ❌ | 联系电话 |
| `email` | string | ❌ | 邮箱地址 |
| `location` | string | ❌ | 所在城市 |
| `is_fresh_graduate` | boolean | ❌ | 是否应届生 |
| `summary` | string | ❌ | 个人简介（1-2句话） |
| `education` | array | ❌ | 教育经历列表 |
| `projects` | array | ❌ | 项目经历列表 |
| `experience` | array | ❌ | 工作经历列表 |
| `skills` | array | ❌ | 技能列表 |
| `other` | array | ❌ | 其他信息（奖学金、证书等） |

### 示例文件位置

参考 `examples/` 目录下的示例文件：
- `examples/resume_data_example.json` - 标准格式示例
- `examples/fresh_graduate_example.json` - 应届生示例
- `examples/experienced_example.json` - 有经验求职者示例

---

## 能力提升计划格式 (growth_plan.json)

代理5（能力提升代理）完成后会自动生成此格式。

### 完整示例

```json
{
  "target_position": "目标岗位",
  "current_level": "当前水平",
  "timeline": "提升周期（如6个月）",
  "phases": [
    {
      "phase": "第1-2个月",
      "title": "阶段标题",
      "goals": ["目标1", "目标2"],
      "tasks": [
        {
          "task": "具体任务",
          "deadline": "截止时间",
          "resources": ["学习资源1", "学习资源2"]
        }
      ],
      "milestone": "里程碑检查标准"
    }
  ]
}
```

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `target_position` | string | ✅ | 目标岗位名称 |
| `current_level` | string | ✅ | 当前能力水平评估 |
| `timeline` | string | ✅ | 整体提升周期 |
| `phases` | array | ✅ | 分阶段计划列表 |
| `phases[].phase` | string | ✅ | 阶段时间范围 |
| `phases[].title` | string | ✅ | 阶段标题 |
| `phases[].goals` | array | ✅ | 该阶段目标列表 |
| `phases[].tasks` | array | ✅ | 具体任务列表 |
| `phases[].milestone` | string | ✅ | 里程碑检查标准 |

### 示例文件位置

参考 `examples/growth_plan_example.json`

---

## 脚本使用说明

### 简历生成脚本

使用上述JSON格式数据生成各种格式的简历文件：

```bash
# 生成HTML简历（推荐）
python scripts/current/create_web_resume.py --data resume_data.json --output resume.html

# 生成PDF简历
python scripts/current/create_pdf_resume.py --data resume_data.json --output resume.pdf

# 生成DOCX简历
python scripts/current/create_docx_resume.py output.docx --data resume_data.json
```

### 能力提升追踪表生成脚本

使用能力提升计划JSON生成Excel追踪表：

```bash
python scripts/current/create_growth_tracker.py --plan growth_plan.json --output tracker.xlsx
```

---

## 数据验证

### JSON语法检查

使用以下方法验证JSON格式是否正确：

```python
import json

# 验证JSON文件
with open('resume_data.json', 'r', encoding='utf-8') as f:
    try:
        data = json.load(f)
        print("✅ JSON格式正确")
    except json.JSONDecodeError as e:
        print(f"❌ JSON格式错误: {e}")
```

### 常见格式错误

1. **缺少逗号**：对象或数组元素之间缺少逗号
2. **多余逗号**：最后一个元素后有多余逗号（JSON标准不允许）
3. **引号不匹配**：字符串必须使用双引号，不能使用单引号
4. **缺少括号**：对象的 `{}` 或数组的 `[]` 不匹配
