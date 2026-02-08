import pdfplumber

def pdf_to_text(src_path, dest_path):
    with pdfplumber.open(src_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted text to {dest_path}")

# Convert Sharia PDF
pdf_to_text("books/sharia/legal_maxims.pdf", "books/sharia/legal_maxims.txt")

# Convert Hanafi Fiqh PDF
pdf_to_text("books/hanafi/quduri.pdf", "books/hanafi/quduri.txt")
