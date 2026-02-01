#!/usr/bin/env python3
"""
Generate PDF resume directly from JSON data using reportlab.
This bypasses HTML rendering issues and ensures consistent output.

Usage:
    python create_pdf_resume_direct.py --data resume_data.json --output resume.pdf
"""

import json
import argparse
import sys
from pathlib import Path

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm, inch
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


def register_chinese_fonts():
    """Register Chinese fonts for proper rendering."""
    # Try multiple font sources in order of preference
    font_paths = [
        # Downloaded font (highest priority)
        '/tmp/fonts/NotoSansCJKsc-Regular.otf',
        # System fonts
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/noto-cjk/NotoSansCJK-Regular.ttc',
        '/System/Library/Fonts/PingFang.ttc',  # Mac
        'C:\\Windows\\Fonts\\msyh.ttc',  # Windows - Microsoft YaHei
    ]

    for font_path in font_paths:
        try:
            if Path(font_path).exists():
                pdfmetrics.registerFont(TTFont('Chinese', font_path))
                print(f"✓ Using font: {font_path}")
                return 'Chinese'
        except Exception as e:
            print(f"✗ Failed to load {font_path}: {e}")
            continue

    # Fallback - download font if not found
    print("⚠ No Chinese font found, attempting to download...")
    try:
        import urllib.request
        download_path = '/tmp/fonts/NotoSansCJKsc-Regular.otf'
        Path(download_path).parent.mkdir(parents=True, exist_ok=True)

        if not Path(download_path).exists():
            url = 'https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.otf'
            print(f"Downloading font from {url}...")
            urllib.request.urlretrieve(url, download_path)

        if Path(download_path).exists():
            pdfmetrics.registerFont(TTFont('Chinese', download_path))
            print(f"✓ Downloaded and using font: {download_path}")
            return 'Chinese'
    except Exception as e:
        print(f"✗ Failed to download font: {e}")

    # Last resort - use Helvetica (Chinese will show as boxes)
    print("⚠ Using Helvetica - Chinese characters may not display correctly")
    return 'Helvetica'


def create_pdf_resume(data: dict, output_path: str) -> None:
    """
    Create a professional PDF resume from structured data.

    Args:
        data: Resume data dictionary
        output_path: Output PDF file path
    """
    # Create PDF
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )

    # Register fonts
    chinese_font = register_chinese_fonts()

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles with Chinese font support
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=chinese_font,
        fontSize=24,
        textColor=colors.HexColor('#1f2937'),
        alignment=TA_CENTER,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=12,
        textColor=colors.HexColor('#6b7280'),
        alignment=TA_CENTER,
        spaceAfter=4
    )

    contact_style = ParagraphStyle(
        'CustomContact',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=9,
        textColor=colors.HexColor('#6b7280'),
        alignment=TA_CENTER,
        spaceAfter=12
    )

    section_title_style = ParagraphStyle(
        'CustomSectionTitle',
        parent=styles['Heading2'],
        fontName=chinese_font,
        fontSize=14,
        textColor=colors.HexColor('#2563eb'),
        spaceBefore=12,
        spaceAfter=8,
        borderPadding=2,
        leftIndent=0
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=10,
        textColor=colors.HexColor('#1f2937'),
        leading=14,
        spaceAfter=6
    )

    entry_title_style = ParagraphStyle(
        'CustomEntryTitle',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=11,
        textColor=colors.HexColor('#1f2937'),
        leading=14,
        fontWeight='bold',
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName=chinese_font,
        fontSize=9,
        textColor=colors.HexColor('#374151'),
        leading=12,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=3
    )

    # Build document content
    content = []

    # Header - Name and Title
    content.append(Paragraph(data.get('name', ''), title_style))
    if data.get('title'):
        content.append(Paragraph(data['title'], subtitle_style))

    # Contact Information
    contact_parts = []
    if data.get('phone'):
        contact_parts.append(data['phone'])
    if data.get('email'):
        contact_parts.append(data['email'])
    if data.get('location'):
        contact_parts.append(data['location'])

    if contact_parts:
        contact_text = ' | '.join(contact_parts)
        content.append(Paragraph(contact_text, contact_style))

    content.append(Spacer(1, 4*mm))

    # Determine section order
    is_fresh_graduate = data.get('is_fresh_graduate', False)

    # Summary
    if data.get('summary'):
        content.append(Paragraph('个人简介', section_title_style))
        content.append(Paragraph(data['summary'], body_style))
        content.append(Spacer(1, 3*mm))

    # Section order based on user status
    if is_fresh_graduate:
        sections = ['education', 'experience', 'projects']
    else:
        sections = ['experience', 'projects', 'education']

    for section_key in sections:
        if section_key == 'education' and data.get('education'):
            add_education_section(content, data['education'], section_title_style, entry_title_style, body_style)
        elif section_key == 'experience' and data.get('experience'):
            add_experience_section(content, data['experience'], section_title_style, entry_title_style, bullet_style)
        elif section_key == 'projects' and data.get('projects'):
            add_projects_section(content, data['projects'], section_title_style, entry_title_style, bullet_style)

    # Skills
    if data.get('skills'):
        add_skills_section(content, data['skills'], section_title_style, body_style)

    # Other
    if data.get('other'):
        content.append(Paragraph('其他', section_title_style))
        for item in data['other']:
            content.append(Paragraph(f'• {item}', bullet_style))
        content.append(Spacer(1, 3*mm))

    # Build PDF
    doc.build(content)
    print(f"✅ PDF resume generated: {output_path}")
    print(f"📄 Direct PDF generation - consistent formatting guaranteed")


def add_education_section(content, education, section_style, title_style, body_style):
    """Add education section to PDF."""
    content.append(Paragraph('教育背景', section_style))

    for edu in education:
        # School and degree on one line
        school_text = f"<b>{edu.get('school', '')}</b> | {edu.get('degree', '')} · {edu.get('major', '')}"
        content.append(Paragraph(school_text, title_style))

        # Date
        if edu.get('startDate') or edu.get('endDate'):
            date_text = f"{edu.get('startDate', '')} - {edu.get('endDate', '')}"
            content.append(Paragraph(date_text, body_style))

        if edu.get('gpa'):
            content.append(Paragraph(f"GPA: {edu['gpa']}", body_style))

        content.append(Spacer(1, 2*mm))

    content.append(Spacer(1, 3*mm))


def add_experience_section(content, experience, section_style, title_style, bullet_style):
    """Add work experience section to PDF."""
    content.append(Paragraph('工作经历', section_style))

    for exp in experience:
        # Company and position
        exp_text = f"<b>{exp.get('company', '')}</b> | {exp.get('position', '')}"
        content.append(Paragraph(exp_text, title_style))

        # Date
        if exp.get('startDate') or exp.get('endDate'):
            date_text = f"{exp.get('startDate', '')} - {exp.get('endDate', '')}"
            content.append(Paragraph(date_text, bullet_style))

        # Achievements
        if exp.get('achievements'):
            for achievement in exp['achievements']:
                content.append(Paragraph(f'• {achievement}', bullet_style))

        content.append(Spacer(1, 2*mm))

    content.append(Spacer(1, 3*mm))


def add_projects_section(content, projects, section_style, title_style, bullet_style):
    """Add projects section to PDF."""
    content.append(Paragraph('项目经验', section_style))

    for proj in projects:
        # Project name and role
        proj_text = f"<b>{proj.get('name', '')}</b>"
        if proj.get('role'):
            proj_text += f" | {proj['role']}"
        content.append(Paragraph(proj_text, title_style))

        # Date
        if proj.get('date'):
            content.append(Paragraph(proj['date'], bullet_style))

        # Tech stack
        if proj.get('tech'):
            tech_list = proj['tech'] if isinstance(proj['tech'], list) else [proj['tech']]
            tech_text = f"技术栈: {', '.join(tech_list)}"
            content.append(Paragraph(tech_text, bullet_style))

        # Details
        if proj.get('details'):
            for detail in proj['details']:
                content.append(Paragraph(f'• {detail}', bullet_style))

        content.append(Spacer(1, 2*mm))

    content.append(Spacer(1, 3*mm))


def add_skills_section(content, skills, section_style, body_style):
    """Add skills section to PDF."""
    content.append(Paragraph('技能清单', section_style))

    for skill in skills:
        skill_text = f"<b>{skill.get('category', '')}:</b> {skill.get('items', '')}"
        content.append(Paragraph(skill_text, body_style))

    content.append(Spacer(1, 3*mm))


def main():
    parser = argparse.ArgumentParser(description="Generate PDF resume directly from JSON data")
    parser.add_argument("--data", "-d", required=True, help="JSON file with resume data")
    parser.add_argument("--output", "-o", default="resume.pdf", help="Output PDF file path")

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

    create_pdf_resume(data, args.output)


if __name__ == "__main__":
    main()
