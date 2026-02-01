#!/usr/bin/env python3
"""
⚠️ DEPRECATED - 此脚本已废弃 ⚠️

此脚本使用 weasyprint 生成PDF，已被新版本替代。

使用新版本:
    scripts/current/create_pdf_resume.py

废弃原因:
    - weasyprint 依赖复杂，安装困难
    - 新版使用 fpdf2，更轻量级
    - 更好的中文支持

废弃时间: v2.0.0 (2026-02-01)
保留原因: 向后兼容和参考

---

Generate PDF resume from HTML content using weasyprint.

Usage:
    python create_pdf_resume.py input.html output.pdf

Dependencies:
    pip install weasyprint
"""

import sys
import argparse
from pathlib import Path

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("Error: weasyprint is required. Install with: pip install weasyprint")
    sys.exit(1)


def create_pdf(input_html: str, output_pdf: str, extra_css: str = None) -> None:
    """
    Convert HTML file or string to PDF.

    Args:
        input_html: Path to HTML file or HTML string content
        output_pdf: Output PDF file path
        extra_css: Optional additional CSS string
    """
    input_path = Path(input_html)

    if input_path.exists():
        # Input is a file path
        html = HTML(filename=str(input_path))
    else:
        # Input is HTML string
        html = HTML(string=input_html)

    stylesheets = []
    if extra_css:
        stylesheets.append(CSS(string=extra_css))

    # Add print-optimized styles
    print_css = CSS(string="""
        @page {
            size: A4;
            margin: 15mm 15mm 15mm 15mm;
        }
        body {
            padding: 0;
            background: white !important;
        }
        /* Force light mode for PDF */
        :root, [data-theme="dark"] {
            --primary-color: #2563eb !important;
            --text-primary: #1f2937 !important;
            --text-secondary: #6b7280 !important;
            --bg-primary: #ffffff !important;
            --bg-secondary: #f9fafb !important;
            --border-color: #e5e7eb !important;
            --shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
        }
        /* Hide toolbar in PDF */
        .toolbar {
            display: none !important;
        }
        /* Ensure proper contrast */
        * {
            color: #1f2937 !important;
            background: transparent !important;
        }
        .resume {
            background: white !important;
        }
        .header {
            background: transparent !important;
        }
    """)
    stylesheets.append(print_css)

    html.write_pdf(output_pdf, stylesheets=stylesheets)
    print(f"PDF generated: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(description="Generate PDF resume from HTML")
    parser.add_argument("input", help="Input HTML file path or HTML string")
    parser.add_argument("output", help="Output PDF file path")
    parser.add_argument("--css", help="Additional CSS file or string", default=None)

    args = parser.parse_args()

    extra_css = None
    if args.css:
        css_path = Path(args.css)
        if css_path.exists():
            extra_css = css_path.read_text()
        else:
            extra_css = args.css

    create_pdf(args.input, args.output, extra_css)


if __name__ == "__main__":
    main()
