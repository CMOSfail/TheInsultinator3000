"""
Creates a polished PDF insult letter styled like an official corporate document.
"""

import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch

from insult_generator.templates import (
    get_random_greeting,
    get_random_insult,
    get_random_company,
    get_random_title,
    get_random_signature
)

FONT_NAME = "Almoni"
FONT_PATH = "resources/fonts/Almoni.ttf"
PROJECT_NAME = "TheInsultinator3000"


def create_insult_pdf(name: str, insult: str = None) -> str:
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(f"Font file not found at {FONT_PATH}")

    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

    # Professional filename based on timestamp and name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = name.replace(" ", "_")
    pdf_filename = f"Letter_of_Professional_Disrespect_{safe_name}_{timestamp}.pdf"

    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    margin = inch

    # Company and header
    company = get_random_company()
    c.setFont(FONT_NAME, 18)
    c.drawString(margin, height - margin, company)

    c.setFont(FONT_NAME, 10)
    c.drawString(margin, height - margin - 15, f"Internal Memorandum | {datetime.now().strftime('%B %d, %Y')}")
    c.line(margin, height - margin - 20, width - margin, height - margin - 20)

    # Body text
    c.setFont(FONT_NAME, 13)
    y = height - margin - 60
    line_spacing = 22

    greeting = get_random_greeting(name)
    c.drawString(margin, y, greeting)
    y -= line_spacing * 2

    if not insult:
        insult = get_random_insult(name)

    # Wrap text to fit page width and avoid word splitting
    max_line_length = 90
    words = insult.split()
    current_line = ""
    
    for word in words:
        # Try to add the word to the current line
        test_line = current_line + " " + word if current_line else word
        
        # If the line exceeds max length, start a new line
        if c.stringWidth(test_line, FONT_NAME, 13) > (width - 2 * margin):
            c.drawString(margin, y, current_line)
            y -= line_spacing
            current_line = word  # Start a new line with the current word
        else:
            current_line = test_line

    # Draw the last line
    if current_line:
        c.drawString(margin, y, current_line)

    y -= line_spacing  # Add a line space before the signature
    
    # Signature
    signature = get_random_signature()
    title = get_random_title()

    c.setFont(FONT_NAME, 12)
    c.drawString(margin, y, signature)
    y -= line_spacing
    c.drawString(margin, y, f"{PROJECT_NAME} — {title}")

    c.save()
    return pdf_filename