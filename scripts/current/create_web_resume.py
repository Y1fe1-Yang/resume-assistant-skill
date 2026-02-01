#!/usr/bin/env python3
"""
Generate web-based HTML resume from JSON data.

Usage:
    python create_web_resume.py --data resume_data.json --output resume.html

Features:
    - Modern responsive design
    - Dark mode support
    - Print optimized
    - Mobile friendly
"""

import json
import argparse
import sys
import re
from pathlib import Path


def render_template(template_content: str, data: dict) -> str:
    """
    Template rendering with proper nested {{#each}} and {{#if}} support.

    Supports:
    - {{variable}} - Simple variable substitution
    - {{#if variable}} ... {{/if}} - Conditional blocks
    - {{#each array}} ... {{/each}} - Array iteration (with nesting support)
    """

    def find_matching_end(text, start_pos, start_tag, end_tag):
        """Find the matching end tag for a given start tag, accounting for nesting."""
        depth = 1
        pos = start_pos

        while depth > 0 and pos < len(text):
            # Find next occurrence of either start or end tag
            next_start = text.find(start_tag, pos)
            next_end = text.find(end_tag, pos)

            if next_end == -1:
                return -1  # No matching end found

            if next_start != -1 and next_start < next_end:
                # Found nested start tag
                depth += 1
                pos = next_start + len(start_tag)
            else:
                # Found end tag
                depth -= 1
                if depth == 0:
                    return next_end
                pos = next_end + len(end_tag)

        return -1

    def process(text, ctx):
        """Process template recursively."""
        # Try to find {{#each}} blocks
        each_start_pattern = r'\{\{#each\s+(\w+)\}\}'
        each_match = re.search(each_start_pattern, text)

        if each_match:
            var_name = each_match.group(1)
            content_start = each_match.end()

            # Find matching {{/each}}
            end_pos = find_matching_end(text, content_start, '{{#each', '{{/each}}')

            if end_pos != -1:
                content = text[content_start:end_pos]
                array = ctx.get(var_name, [])

                if isinstance(array, list) and len(array) > 0:
                    parts = []
                    for item in array:
                        item_ctx = dict(ctx)
                        if isinstance(item, dict):
                            item_ctx.update(item)
                        else:
                            item_ctx['this'] = item

                        rendered = process(content, item_ctx)
                        parts.append(rendered)

                    replacement = ''.join(parts)
                else:
                    replacement = ''

                # Replace and continue
                before = text[:each_match.start()]
                after = text[end_pos + len('{{/each}}'):]
                text = before + replacement + after
                return process(text, ctx)

        # Try to find {{#if}} blocks
        if_start_pattern = r'\{\{#if\s+(\w+)\}\}'
        if_match = re.search(if_start_pattern, text)

        if if_match:
            var_name = if_match.group(1)
            content_start = if_match.end()

            end_pos = find_matching_end(text, content_start, '{{#if', '{{/if}}')

            if end_pos != -1:
                content = text[content_start:end_pos]
                value = ctx.get(var_name)

                if value and (not isinstance(value, (list, str)) or len(value) > 0):
                    replacement = process(content, ctx)
                else:
                    replacement = ''

                before = text[:if_match.start()]
                after = text[end_pos + len('{{/if}}'):]
                text = before + replacement + after
                return process(text, ctx)

        # Replace variables
        def replace_var(m):
            var_name = m.group(1).strip()
            value = ctx.get(var_name, '')
            return str(value) if value is not None else ''

        text = re.sub(r'\{\{(?!#|/)([^\}]+)\}\}', replace_var, text)

        return text

    return process(template_content, data)


def create_web_resume(data: dict, output_path: str, template: str = 'modern') -> None:
    """
    Create a web-based HTML resume from structured data.

    Args:
        data: Resume data dictionary
        output_path: Output HTML file path
        template: Template name ('modern' or 'minimal')
    """
    # Get script directory
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent

    # Determine section order based on user status
    # If user is fresh graduate, put education before work experience
    is_fresh_graduate = data.get('is_fresh_graduate', False)

    # Create section order hint for template (for informational purposes)
    data['_section_order_hint'] = 'education_first' if is_fresh_graduate else 'experience_first'

    # Load template
    if template == 'modern':
        template_path = skill_dir / 'assets' / 'templates' / 'web-resume-modern.html'
    else:
        # Fallback to modern if template not found
        template_path = skill_dir / 'assets' / 'templates' / 'web-resume-modern.html'

    if not template_path.exists():
        print(f"Error: Template not found: {template_path}")
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Adjust template section order based on user status
    if is_fresh_graduate:
        # Move education section before work experience for fresh graduates
        template_content = reorder_sections_for_fresh_grad(template_content)

    # Render template with data
    html_content = render_template(template_content, data)

    # Write output
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Web resume generated: {output_path}")
    print(f"💡 Open in browser: file://{output_file.absolute()}")
    print(f"📱 Responsive design: works on mobile and desktop")
    print(f"🌙 Dark mode: click the theme toggle button")
    print(f"📄 Export PDF: click 'Print/Export PDF' or use browser print (Ctrl+P / Cmd+P)")


def reorder_sections_for_fresh_grad(template_html: str) -> str:
    """
    Reorder sections in template to put education before work experience.
    For fresh graduates, education is more important than limited work experience.
    """
    # Find education section
    edu_start = template_html.find('<!-- 教育背景 -->')
    if edu_start == -1:
        return template_html

    # Find end of education section (next section comment or skills)
    edu_end = template_html.find('<!-- 技能清单 -->', edu_start)
    if edu_end == -1:
        return template_html

    education_section = template_html[edu_start:edu_end]

    # Find where to insert (after summary, before work experience)
    summary_end = template_html.find('{{/if}}', template_html.find('<!-- 个人简介 -->'))
    if summary_end == -1:
        return template_html

    insert_pos = summary_end + len('{{/if}}') + 1

    # Remove education from original position
    template_before_edu = template_html[:edu_start]
    template_after_edu = template_html[edu_end:]

    # Insert education after summary
    template_before_insert = template_html[:insert_pos]
    template_after_insert = template_html[insert_pos:edu_start] + template_html[edu_end:]

    return template_before_insert + '\n' + education_section + template_after_insert


def main():
    parser = argparse.ArgumentParser(description="Generate web-based HTML resume from JSON data")
    parser.add_argument("--data", "-d", required=True, help="JSON file with resume data")
    parser.add_argument("--output", "-o", default="resume.html", help="Output HTML file path")
    parser.add_argument("--template", "-t", default="modern", choices=['modern'],
                       help="Template style (default: modern)")

    args = parser.parse_args()

    # Load data
    data_path = Path(args.data)
    if not data_path.exists():
        print(f"Error: Data file not found: {args.data}")
        sys.exit(1)

    with open(data_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {args.data}: {e}")
            sys.exit(1)

    create_web_resume(data, args.output, args.template)


if __name__ == "__main__":
    main()
