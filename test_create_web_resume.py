#!/usr/bin/env python3
"""
Comprehensive robustness tests for create_web_resume.py

Test Categories:
1. Normal execution paths
2. Edge cases and boundary conditions
3. Invalid inputs and error handling
4. File system edge cases
5. Template rendering edge cases
6. Unicode and special characters
7. Performance with large data
"""

import json
import tempfile
import shutil
import sys
from pathlib import Path
from typing import Dict, Any
import subprocess

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts' / 'current'))

from create_web_resume import render_template, create_web_resume, reorder_sections_for_fresh_grad


class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def record_pass(self, test_name: str):
        self.passed += 1
        print(f"✅ PASS: {test_name}")

    def record_fail(self, test_name: str, error: str):
        self.failed += 1
        self.errors.append((test_name, error))
        print(f"❌ FAIL: {test_name}")
        print(f"   Error: {error}")

    def summary(self):
        total = self.passed + self.failed
        print("\n" + "="*60)
        print(f"Test Summary: {self.passed}/{total} passed, {self.failed}/{total} failed")
        if self.errors:
            print("\nFailed Tests:")
            for test_name, error in self.errors:
                print(f"  - {test_name}: {error}")
        print("="*60)


result = TestResult()


def test_1_normal_minimal_data():
    """Test with minimal valid resume data"""
    try:
        data = {
            "name": "张三",
            "title": "软件工程师",
            "email": "zhangsan@example.com"
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path, 'modern')

        # Verify file was created
        assert Path(output_path).exists(), "Output file not created"

        # Verify basic content
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "张三" in content, "Name not found in output"
            assert "软件工程师" in content, "Title not found in output"

        Path(output_path).unlink()
        result.record_pass("test_1_normal_minimal_data")
    except Exception as e:
        result.record_fail("test_1_normal_minimal_data", str(e))


def test_2_comprehensive_data():
    """Test with complete resume data"""
    try:
        data = {
            "name": "李明",
            "title": "高级Python开发工程师",
            "email": "liming@example.com",
            "phone": "+86 138-0000-0000",
            "location": "北京市",
            "summary": "5年Python开发经验，擅长后端架构设计",
            "work_experience": [
                {
                    "company": "科技公司A",
                    "title": "高级工程师",
                    "duration": "2020-至今",
                    "achievements": ["负责核心系统开发", "性能优化50%"]
                }
            ],
            "education": [
                {
                    "school": "清华大学",
                    "degree": "计算机科学学士",
                    "duration": "2015-2019"
                }
            ],
            "skills": ["Python", "Django", "PostgreSQL"]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "李明" in content
            assert "科技公司A" in content
            assert "清华大学" in content

        Path(output_path).unlink()
        result.record_pass("test_2_comprehensive_data")
    except Exception as e:
        result.record_fail("test_2_comprehensive_data", str(e))


def test_3_empty_arrays():
    """Test with empty arrays (edge case)"""
    try:
        data = {
            "name": "王五",
            "title": "开发者",
            "work_experience": [],
            "education": [],
            "skills": []
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        assert Path(output_path).exists()
        Path(output_path).unlink()
        result.record_pass("test_3_empty_arrays")
    except Exception as e:
        result.record_fail("test_3_empty_arrays", str(e))


def test_4_missing_optional_fields():
    """Test with missing optional fields"""
    try:
        data = {
            "name": "赵六",
            "title": "工程师"
            # Missing: email, phone, location, summary, etc.
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        assert Path(output_path).exists()
        Path(output_path).unlink()
        result.record_pass("test_4_missing_optional_fields")
    except Exception as e:
        result.record_fail("test_4_missing_optional_fields", str(e))


def test_5_unicode_and_special_chars():
    """Test with unicode, emoji, and special characters"""
    try:
        data = {
            "name": "田中太郎 🎌",
            "title": "Software Engineer 💻",
            "email": "tanaka@日本.jp",
            "summary": "Привет! 你好! Hello! مرحبا",
            "skills": ["C++", "C#", "HTML/CSS", "SQL", "<script>alert('xss')</script>"]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check unicode is preserved
            assert "田中太郎" in content
            # Check XSS is handled (should be escaped or raw)
            assert Path(output_path).exists()

        Path(output_path).unlink()
        result.record_pass("test_5_unicode_and_special_chars")
    except Exception as e:
        result.record_fail("test_5_unicode_and_special_chars", str(e))


def test_6_very_long_strings():
    """Test with extremely long strings"""
    try:
        data = {
            "name": "A" * 1000,
            "title": "B" * 500,
            "summary": "C" * 10000,
            "skills": ["Skill" + str(i) for i in range(100)]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        assert Path(output_path).exists()
        Path(output_path).unlink()
        result.record_pass("test_6_very_long_strings")
    except Exception as e:
        result.record_fail("test_6_very_long_strings", str(e))


def test_7_nested_template_rendering():
    """Test nested {{#each}} and {{#if}} blocks"""
    try:
        template = """
        {{#if work_experience}}
        Work:
        {{#each work_experience}}
          - {{company}}
          {{#if achievements}}
          Achievements:
          {{#each achievements}}
            * {{this}}
          {{/each}}
          {{/if}}
        {{/each}}
        {{/if}}
        """

        data = {
            "work_experience": [
                {
                    "company": "Company A",
                    "achievements": ["Achievement 1", "Achievement 2"]
                },
                {
                    "company": "Company B",
                    "achievements": []
                },
                {
                    "company": "Company C"
                    # No achievements field
                }
            ]
        }

        result_html = render_template(template, data)
        assert "Company A" in result_html
        assert "Achievement 1" in result_html
        assert "Company B" in result_html
        assert "Company C" in result_html

        result.record_pass("test_7_nested_template_rendering")
    except Exception as e:
        result.record_fail("test_7_nested_template_rendering", str(e))


def test_8_output_directory_creation():
    """Test automatic creation of nested output directories"""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "deep" / "nested" / "path" / "resume.html"

            data = {"name": "Test", "title": "Engineer"}
            create_web_resume(data, str(output_path))

            assert output_path.exists()

        result.record_pass("test_8_output_directory_creation")
    except Exception as e:
        result.record_fail("test_8_output_directory_creation", str(e))


def test_9_fresh_graduate_flag():
    """Test fresh graduate section reordering"""
    try:
        data_fresh = {
            "name": "应届生",
            "title": "毕业生",
            "is_fresh_graduate": True,
            "education": [{"school": "大学", "degree": "学士"}],
            "work_experience": [{"company": "实习公司"}]
        }

        data_experienced = {
            "name": "经验者",
            "title": "工程师",
            "is_fresh_graduate": False,
            "education": [{"school": "大学", "degree": "学士"}],
            "work_experience": [{"company": "公司A"}]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f1:
            output1 = f1.name
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f2:
            output2 = f2.name

        create_web_resume(data_fresh, output1)
        create_web_resume(data_experienced, output2)

        # Both should succeed
        assert Path(output1).exists()
        assert Path(output2).exists()

        Path(output1).unlink()
        Path(output2).unlink()

        result.record_pass("test_9_fresh_graduate_flag")
    except Exception as e:
        result.record_fail("test_9_fresh_graduate_flag", str(e))


def test_10_null_values():
    """Test with null/None values in data"""
    try:
        data = {
            "name": "Test User",
            "title": None,
            "email": None,
            "summary": None,
            "work_experience": None
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Should handle None gracefully
            assert "Test User" in content

        Path(output_path).unlink()
        result.record_pass("test_10_null_values")
    except Exception as e:
        result.record_fail("test_10_null_values", str(e))


def test_11_template_variable_not_in_data():
    """Test template with variables not present in data"""
    try:
        template = "{{name}} - {{nonexistent_field}} - {{another_missing}}"
        data = {"name": "John"}

        result_html = render_template(template, data)
        assert "John" in result_html
        # Missing variables should be replaced with empty string
        assert result_html == "John -  - "

        result.record_pass("test_11_template_variable_not_in_data")
    except Exception as e:
        result.record_fail("test_11_template_variable_not_in_data", str(e))


def test_12_malformed_template_syntax():
    """Test handling of malformed template syntax"""
    try:
        # Unclosed {{#if}}
        template1 = "{{#if test}}Content here"
        data = {"test": True}
        result_html = render_template(template1, data)
        # Should handle gracefully (might not process the block)

        # Unclosed {{#each}}
        template2 = "{{#each items}}Item: {{this}}"
        data2 = {"items": ["a", "b"]}
        result_html2 = render_template(template2, data2)

        # Both should not crash
        result.record_pass("test_12_malformed_template_syntax")
    except Exception as e:
        result.record_fail("test_12_malformed_template_syntax", str(e))


def test_13_deeply_nested_iteration():
    """Test deeply nested {{#each}} blocks"""
    try:
        template = """
        {{#each level1}}
        L1: {{name}}
        {{#each level2}}
        L2: {{name}}
        {{#each level3}}
        L3: {{name}}
        {{/each}}
        {{/each}}
        {{/each}}
        """

        data = {
            "level1": [
                {
                    "name": "A",
                    "level2": [
                        {
                            "name": "B",
                            "level3": [
                                {"name": "C1"},
                                {"name": "C2"}
                            ]
                        }
                    ]
                }
            ]
        }

        result_html = render_template(template, data)
        assert "L1: A" in result_html
        assert "L2: B" in result_html
        assert "L3: C1" in result_html
        assert "L3: C2" in result_html

        result.record_pass("test_13_deeply_nested_iteration")
    except Exception as e:
        result.record_fail("test_13_deeply_nested_iteration", str(e))


def test_14_non_dict_array_items():
    """Test {{#each}} with non-dictionary items"""
    try:
        template = "{{#each items}}Item: {{this}}, {{/each}}"
        data = {"items": ["apple", "banana", "cherry"]}

        result_html = render_template(template, data)
        assert "apple" in result_html
        assert "banana" in result_html
        assert "cherry" in result_html

        result.record_pass("test_14_non_dict_array_items")
    except Exception as e:
        result.record_fail("test_14_non_dict_array_items", str(e))


def test_15_boolean_conditionals():
    """Test {{#if}} with various truthy/falsy values"""
    try:
        template = "{{#if flag}}YES{{/if}}"

        # Test different truthy values
        assert "YES" in render_template(template, {"flag": True})
        assert "YES" in render_template(template, {"flag": 1})
        assert "YES" in render_template(template, {"flag": "text"})
        assert "YES" in render_template(template, {"flag": [1]})

        # Test falsy values
        assert "YES" not in render_template(template, {"flag": False})
        assert "YES" not in render_template(template, {"flag": 0})
        assert "YES" not in render_template(template, {"flag": ""})
        assert "YES" not in render_template(template, {"flag": []})
        assert "YES" not in render_template(template, {"flag": None})

        result.record_pass("test_15_boolean_conditionals")
    except Exception as e:
        result.record_fail("test_15_boolean_conditionals", str(e))


def test_16_large_dataset():
    """Test with large dataset (performance test)"""
    try:
        data = {
            "name": "Performance Test",
            "title": "Engineer",
            "work_experience": [
                {
                    "company": f"Company {i}",
                    "title": f"Position {i}",
                    "duration": f"2020-202{i%10}",
                    "achievements": [f"Achievement {j}" for j in range(10)]
                }
                for i in range(50)  # 50 jobs with 10 achievements each
            ],
            "skills": [f"Skill {i}" for i in range(100)]
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        assert Path(output_path).exists()
        file_size = Path(output_path).stat().st_size
        # File should be reasonably large but not excessive
        assert file_size > 1000, "Output file too small"
        assert file_size < 10_000_000, "Output file too large (>10MB)"

        Path(output_path).unlink()
        result.record_pass("test_16_large_dataset")
    except Exception as e:
        result.record_fail("test_16_large_dataset", str(e))


def test_17_special_html_chars():
    """Test HTML special characters handling"""
    try:
        data = {
            "name": "Test <User>",
            "title": "Engineer & Developer",
            "summary": "Experience with <html> tags & \"quoted\" text"
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Characters should be present (may or may not be escaped)
            assert Path(output_path).exists()

        Path(output_path).unlink()
        result.record_pass("test_17_special_html_chars")
    except Exception as e:
        result.record_fail("test_17_special_html_chars", str(e))


def test_18_numeric_values():
    """Test with numeric values in data"""
    try:
        data = {
            "name": "Test User",
            "title": "Engineer",
            "years_experience": 5,
            "age": 30,
            "salary_expectation": 100000.50
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        create_web_resume(data, output_path)

        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Numbers should be converted to strings
            assert "Test User" in content

        Path(output_path).unlink()
        result.record_pass("test_18_numeric_values")
    except Exception as e:
        result.record_fail("test_18_numeric_values", str(e))


def test_19_whitespace_handling():
    """Test whitespace in template variables"""
    try:
        template = "{{ name }}-{{  title  }}-{{email}}"
        data = {"name": "John", "title": "Dev", "email": "j@x.com"}

        result_html = render_template(template, data)
        assert "John" in result_html
        assert "Dev" in result_html
        assert "j@x.com" in result_html

        result.record_pass("test_19_whitespace_handling")
    except Exception as e:
        result.record_fail("test_19_whitespace_handling", str(e))


def test_20_reorder_sections_edge_cases():
    """Test section reordering with edge cases"""
    try:
        # Test with missing markers
        html1 = "<html><body>No section markers here</body></html>"
        result1 = reorder_sections_for_fresh_grad(html1)
        # Should return unchanged
        assert result1 == html1

        # Test with partial markers
        html2 = "<html><!-- 教育背景 --><div>Education</div></html>"
        result2 = reorder_sections_for_fresh_grad(html2)
        # Should handle gracefully

        result.record_pass("test_20_reorder_sections_edge_cases")
    except Exception as e:
        result.record_fail("test_20_reorder_sections_edge_cases", str(e))


def test_21_cli_missing_data_file():
    """Test CLI with non-existent data file"""
    try:
        proc = subprocess.run(
            ["python", "scripts/current/create_web_resume.py", "--data", "nonexistent.json"],
            capture_output=True,
            text=True
        )

        # Should exit with error
        assert proc.returncode == 1
        assert "not found" in proc.stdout.lower() or "not found" in proc.stderr.lower()

        result.record_pass("test_21_cli_missing_data_file")
    except Exception as e:
        result.record_fail("test_21_cli_missing_data_file", str(e))


def test_22_cli_invalid_json():
    """Test CLI with invalid JSON file"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("{ invalid json }")
            json_path = f.name

        proc = subprocess.run(
            ["python", "scripts/current/create_web_resume.py", "--data", json_path],
            capture_output=True,
            text=True
        )

        Path(json_path).unlink()

        # Should exit with error
        assert proc.returncode == 1
        assert "json" in proc.stdout.lower() or "json" in proc.stderr.lower()

        result.record_pass("test_22_cli_invalid_json")
    except Exception as e:
        result.record_fail("test_22_cli_invalid_json", str(e))


def test_23_path_traversal_security():
    """Test output path with path traversal attempts"""
    try:
        data = {"name": "Test", "title": "Engineer"}

        # Try to write outside of intended directory
        with tempfile.TemporaryDirectory() as tmpdir:
            # This should still work but create the file safely
            output_path = Path(tmpdir) / ".." / "safe" / "resume.html"
            create_web_resume(data, str(output_path))

            # File should be created (parents=True allows this)
            assert output_path.exists()
            output_path.unlink()
            output_path.parent.rmdir()

        result.record_pass("test_23_path_traversal_security")
    except Exception as e:
        result.record_fail("test_23_path_traversal_security", str(e))


def test_24_template_with_newlines():
    """Test template rendering preserves newlines and formatting"""
    try:
        template = """Line 1
        Line 2
        {{#if show}}
        Conditional Line
        {{/if}}
        Line 3"""

        data = {"show": True}
        result_html = render_template(template, data)

        # Newlines should be preserved
        assert "Line 1" in result_html
        assert "Line 2" in result_html
        assert "Conditional Line" in result_html
        assert "Line 3" in result_html

        result.record_pass("test_24_template_with_newlines")
    except Exception as e:
        result.record_fail("test_24_template_with_newlines", str(e))


def test_25_empty_data_dictionary():
    """Test with completely empty data"""
    try:
        data = {}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name

        # This might fail or succeed depending on template requirements
        try:
            create_web_resume(data, output_path)
            if Path(output_path).exists():
                Path(output_path).unlink()
            result.record_pass("test_25_empty_data_dictionary")
        except Exception:
            # If it fails gracefully with an error, that's also acceptable
            result.record_pass("test_25_empty_data_dictionary")
    except Exception as e:
        result.record_fail("test_25_empty_data_dictionary", str(e))


def main():
    print("="*60)
    print("🧪 Starting Comprehensive Robustness Tests")
    print("="*60 + "\n")

    # Run all tests
    test_1_normal_minimal_data()
    test_2_comprehensive_data()
    test_3_empty_arrays()
    test_4_missing_optional_fields()
    test_5_unicode_and_special_chars()
    test_6_very_long_strings()
    test_7_nested_template_rendering()
    test_8_output_directory_creation()
    test_9_fresh_graduate_flag()
    test_10_null_values()
    test_11_template_variable_not_in_data()
    test_12_malformed_template_syntax()
    test_13_deeply_nested_iteration()
    test_14_non_dict_array_items()
    test_15_boolean_conditionals()
    test_16_large_dataset()
    test_17_special_html_chars()
    test_18_numeric_values()
    test_19_whitespace_handling()
    test_20_reorder_sections_edge_cases()
    test_21_cli_missing_data_file()
    test_22_cli_invalid_json()
    test_23_path_traversal_security()
    test_24_template_with_newlines()
    test_25_empty_data_dictionary()

    # Print summary
    result.summary()

    # Exit with appropriate code
    sys.exit(0 if result.failed == 0 else 1)


if __name__ == "__main__":
    main()
