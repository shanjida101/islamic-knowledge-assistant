import pdfplumber
import os

PDF_PATH = "books/hanafi/al_hidayah.pdf"
TXT_PATH = "books/hanafi/al_hidayah.txt"

os.makedirs("books/hanafi", exist_ok=True)

text = ""

with pdfplumber.open(PDF_PATH) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        page_text = page.extract_text()
        if page_text:
            text += f"\n\n--- Page {i} ---\n\n"
            text += page_text

with open(TXT_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Extracted Al-Hidayah text to al_hidayah.txt")
