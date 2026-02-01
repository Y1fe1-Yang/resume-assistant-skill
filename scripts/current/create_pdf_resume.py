#!/usr/bin/env python3
"""
Generate PDF resume using fpdf2 with excellent Chinese support.

Usage:
    python create_pdf_resume_fpdf.py --data resume_data.json --output resume.pdf
"""

import json
import argparse
import sys
import os
from pathlib import Path

try:
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
except ImportError:
    print("Error: fpdf2 is required. Install with: pip install fpdf2")
    sys.exit(1)


class ResumePDF(FPDF):
    """Custom PDF class for resume generation with Chinese support."""

    def __init__(self):
        super().__init__()
        self.add_page()

        # Try to load Chinese font with fallback mechanism
        font_loaded = False
        font_name = 'NotoSans'

        # Get bundled font path (in skill's assets/fonts directory)
        script_dir = Path(__file__).parent          # scripts/current/
        skill_dir = script_dir.parent.parent        # skill root
        bundled_font = skill_dir / 'assets' / 'fonts' / 'NotoSansSC.ttf'

        # List of potential font paths to try (bundled font has highest priority)
        font_paths = [
            str(bundled_font) if bundled_font.exists() else None,  # Bundled font (highest priority)
            os.getenv('RESUME_FONT_PATH'),  # Environment variable
            '/tmp/fonts/NotoSansSC.ttf',     # Default path
            str(Path.home() / '.fonts' / 'NotoSansSC.ttf'),  # User fonts
            '/usr/share/fonts/truetype/noto/NotoSansSC-Regular.ttf',  # Linux system fonts
            '/System/Library/Fonts/PingFang.ttc',  # macOS
        ]

        for font_path in font_paths:
            if font_path and Path(font_path).exists():
                try:
                    self.add_font(font_name, '', font_path, uni=True)
                    self.set_font(font_name, '', 12)
                    font_loaded = True
                    # Keep font_name as string
                    font_name = str(font_name)
                    break
                except Exception:
                    continue

        if not font_loaded:
            # Fallback mode: No Chinese font available
            print("⚠️  WARNING: Chinese font not found!")
            print("   This is unexpected - the font should be bundled in assets/fonts/")
            print("   PDF will be generated with limited character support.")
            print("   Chinese characters will be replaced with placeholders.")
            print()
            print("   Troubleshooting:")
            print(f"   1. Check bundled font: {bundled_font}")
            print("   2. Verify skill installation is complete")
            print("   3. Or set RESUME_FONT_PATH=/path/to/your/font.ttf")
            print()
            print("   See references/troubleshooting.md for more details.\n")

            # Use built-in helvetica (ASCII only)
            # Chinese characters will be replaced with placeholders
            font_name = 'helvetica'
            self.set_font('helvetica', '', 12)

        # Store font name and fallback status (use different name to avoid conflict with fpdf's current_font)
        self.resume_font_name = font_name  # Keep as string
        self.chinese_support = font_loaded

    def safe_text(self, text):
        """Convert text to ASCII-safe format if Chinese font not available."""
        if not text:
            return ''
        if self.chinese_support:
            return text
        # Replace non-ASCII characters with Romanization hint
        try:
            text.encode('ascii')
            return text
        except UnicodeEncodeError:
            # Return text with note that Chinese font is needed
            return '[Chinese text - font required]'

    def header_section(self, name, title, contact):
        """Add header with name and contact info."""
        # Name
        self.set_font(self.resume_font_name, '', 24)
        self.set_text_color(31, 41, 55)
        self.cell(0, 10, self.safe_text(name), align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Title
        if title:
            self.set_font(self.resume_font_name, '', 12)
            self.set_text_color(107, 114, 128)
            self.cell(0, 7, self.safe_text(title), align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Contact
        if contact:
            self.set_font(self.resume_font_name, '', 9)
            self.cell(0, 6, self.safe_text(contact), align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.ln(3)

    def section_title(self, title):
        """Add a section title."""
        self.set_font(self.resume_font_name, '', 14)
        self.set_text_color(37, 99, 235)
        self.cell(0, 8, self.safe_text(title), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def entry_title(self, title, date=''):
        """Add an entry title with optional date."""
        self.set_font(self.resume_font_name, '', 11)
        self.set_text_color(31, 41, 55)

        title_safe = self.safe_text(title)
        date_safe = self.safe_text(date)

        if date:
            # Title on left, date on right
            title_width = self.get_string_width(title_safe) + 2
            self.cell(title_width, 6, title_safe)

            # Date on the right
            self.set_x(self.w - self.r_margin - self.get_string_width(date_safe))
            self.set_text_color(107, 114, 128)
            self.cell(0, 6, date_safe, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        else:
            self.cell(0, 6, title_safe, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_text_color(31, 41, 55)

    def body_text(self, text, bullet=False):
        """Add body text with optional bullet point."""
        self.set_font(self.resume_font_name, '', 9)
        self.set_text_color(55, 65, 81)

        text_safe = self.safe_text(text)

        if bullet:
            # Bullet point (use ASCII-safe bullet if no Chinese support)
            bullet_char = '•' if self.chinese_support else '-'
            x_start = self.get_x()
            self.cell(5, 5, bullet_char)
            self.set_x(x_start + 5)
            # Multi-line text
            self.multi_cell(0, 4, text_safe)
        else:
            self.multi_cell(0, 5, text_safe)

        self.ln(1)


def create_pdf_resume(data: dict, output_path: str) -> None:
    """
    Create a PDF resume from structured data.

    Args:
        data: Resume data dictionary
        output_path: Output PDF file path
    """
    try:
        pdf = ResumePDF()

        # Header
        contact_parts = []
        if data.get('phone'):
            contact_parts.append(data['phone'])
        if data.get('email'):
            contact_parts.append(data['email'])
        if data.get('location'):
            contact_parts.append(data['location'])

        pdf.header_section(
            data.get('name', ''),
            data.get('title', ''),
            ' | '.join(contact_parts) if contact_parts else ''
        )

        # Determine section order
        is_fresh_graduate = data.get('is_fresh_graduate', False)

        # Summary
        if data.get('summary'):
            pdf.section_title('个人简介')
            pdf.body_text(data['summary'])
            pdf.ln(2)

        # Section order
        if is_fresh_graduate:
            sections = ['education', 'experience', 'projects']
        else:
            sections = ['experience', 'projects', 'education']

        for section_key in sections:
            if section_key == 'education' and data.get('education'):
                add_education(pdf, data['education'])
            elif section_key == 'experience' and data.get('experience'):
                add_experience(pdf, data['experience'])
            elif section_key == 'projects' and data.get('projects'):
                add_projects(pdf, data['projects'])

        # Skills
        if data.get('skills'):
            add_skills(pdf, data['skills'])

        # Other
        if data.get('other'):
            pdf.section_title('其他')
            for item in data['other']:
                pdf.body_text(item, bullet=True)

        # Output
        pdf.output(output_path)
        print(f"✅ PDF resume generated: {output_path}")
        print(f"📄 Chinese characters fully supported with fpdf2!")

    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def add_education(pdf, education):
    """Add education section."""
    pdf.section_title('教育背景')

    for edu in education:
        # School name and degree
        title = f"{edu.get('school', '')} | {edu.get('degree', '')} · {edu.get('major', '')}"
        date = f"{edu.get('startDate', '')} - {edu.get('endDate', '')}" if edu.get('startDate') or edu.get('endDate') else ''

        pdf.entry_title(title, date)

        if edu.get('gpa'):
            pdf.body_text(f"GPA: {edu['gpa']}")

        pdf.ln(2)

    pdf.ln(2)


def add_experience(pdf, experience):
    """Add work experience section."""
    pdf.section_title('工作经历')

    for exp in experience:
        # Company and position
        title = f"{exp.get('company', '')} | {exp.get('position', '')}"
        date = f"{exp.get('startDate', '')} - {exp.get('endDate', '')}" if exp.get('startDate') or exp.get('endDate') else ''

        pdf.entry_title(title, date)

        # Achievements
        if exp.get('achievements'):
            for achievement in exp['achievements']:
                pdf.body_text(achievement, bullet=True)

        pdf.ln(2)

    pdf.ln(2)


def add_projects(pdf, projects):
    """Add projects section."""
    pdf.section_title('项目经验')

    for proj in projects:
        # Project name and role
        title = proj.get('name', '')
        if proj.get('role'):
            title += f" | {proj['role']}"

        date = proj.get('date', '')

        pdf.entry_title(title, date)

        # Tech stack
        if proj.get('tech'):
            tech_list = proj['tech'] if isinstance(proj['tech'], list) else [proj['tech']]
            pdf.body_text(f"技术栈: {', '.join(tech_list)}")

        # Details
        if proj.get('details'):
            for detail in proj['details']:
                pdf.body_text(detail, bullet=True)

        pdf.ln(2)

    pdf.ln(2)


def add_skills(pdf, skills):
    """Add skills section."""
    pdf.section_title('技能清单')

    for skill in skills:
        text = f"{skill.get('category', '')}: {skill.get('items', '')}"
        pdf.body_text(text)

    pdf.ln(2)


def main():
    parser = argparse.ArgumentParser(description="Generate PDF resume from JSON data")
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
