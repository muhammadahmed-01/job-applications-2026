#!/usr/bin/env python3
"""Export resume.md to a clean one-page-ish PDF. Usage: md_resume_to_pdf.py <resume.md> [out.pdf]"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


def strip_md_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)


def inline_md(text: str) -> str:
    text = strip_md_links(text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    return text


def md_to_flowables(md: str):
    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name",
        parent=styles["Heading1"],
        fontSize=16,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=4,
        textColor="#111111",
    )
    headline = ParagraphStyle(
        "Headline",
        parent=styles["Normal"],
        fontSize=10,
        leading=13,
        alignment=TA_CENTER,
        spaceAfter=2,
        textColor="#222222",
    )
    contact = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        spaceAfter=8,
        textColor="#333333",
    )
    section = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontSize=11,
        leading=14,
        spaceBefore=8,
        spaceAfter=4,
        textColor="#111111",
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        alignment=TA_LEFT,
        spaceAfter=3,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=12,
        bulletIndent=0,
        spaceAfter=2,
    )
    job = ParagraphStyle(
        "Job",
        parent=body,
        fontSize=9.5,
        leading=12,
        spaceBefore=4,
        spaceAfter=2,
    )

    flow = []
    lines = md.replace("\r\n", "\n").split("\n")
    i = 0
    saw_name = False
    while i < len(lines):
        raw = lines[i].rstrip()
        line = raw.strip()
        if not line or line == "---":
            i += 1
            continue
        if line.startswith("# ") and not saw_name:
            flow.append(Paragraph(inline_md(line[2:]), name))
            saw_name = True
            i += 1
            continue
        if line.startswith("**") and line.endswith("**") and "Engineer" in line:
            flow.append(Paragraph(inline_md(line), headline))
            i += 1
            continue
        if "Lahore" in line or "linkedin" in line.lower() or "@" in line:
            flow.append(Paragraph(inline_md(line), contact))
            flow.append(HRFlowable(width="100%", thickness=0.6, color="#444444", spaceAfter=4))
            i += 1
            continue
        if line.startswith("## "):
            flow.append(Paragraph(inline_md(line[3:].upper()), section))
            flow.append(HRFlowable(width="100%", thickness=0.4, color="#888888", spaceAfter=3))
            i += 1
            continue
        if line.startswith("### "):
            flow.append(Paragraph(inline_md(line[4:]), job))
            i += 1
            continue
        if line.startswith("- "):
            flow.append(Paragraph("• " + inline_md(line[2:]), bullet))
            i += 1
            continue
        flow.append(Paragraph(inline_md(line), body))
        i += 1
    return flow


def export(md_path: Path, pdf_path: Path) -> None:
    md = md_path.read_text(encoding="utf-8")
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        title=pdf_path.stem,
        author="Muhammad Ahmed",
    )
    doc.build(md_to_flowables(md))


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: md_resume_to_pdf.py <resume.md> [out.pdf]", file=sys.stderr)
        return 2
    md_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2]) if len(sys.argv) > 2 else md_path.with_suffix(".pdf")
    export(md_path, pdf_path)
    print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
