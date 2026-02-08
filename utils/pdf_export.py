from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os


def export_results_to_pdf(question, results, filename="islamic_ai_results.pdf"):
    os.makedirs("exports", exist_ok=True)
    path = f"exports/{filename}"

    doc = SimpleDocTemplate(path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Islamic Knowledge Assistant – Results</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"<b>Question:</b> {question}", styles["Normal"]))
    story.append(Paragraph(f"<b>Generated on:</b> {datetime.now()}", styles["Normal"]))
    story.append(Spacer(1, 16))

    for source, answers in results.items():
        story.append(Paragraph(f"<b>{source}</b>", styles["Heading2"]))
        story.append(Spacer(1, 8))

        for ans in answers:
            story.append(Paragraph(ans.replace("<br>", "<br/>"), styles["Normal"]))
            story.append(Spacer(1, 6))

        story.append(Spacer(1, 12))

    doc.build(story)
    return path
