import json

# Replace with your file names
arabic_file = "quran_arabic.txt"
english_file = "quran_english.txt"
bengali_file = "quran_bengali.txt"

# Read files
with open(arabic_file, "r", encoding="utf-8") as f:
    arabic_lines = f.read().splitlines()

with open(english_file, "r", encoding="utf-8") as f:
    english_lines = f.read().splitlines()

with open(bengali_file, "r", encoding="utf-8") as f:
    bengali_lines = f.read().splitlines()

# Sanity check
if not (len(arabic_lines) == len(english_lines) == len(bengali_lines)):
    raise ValueError("❌ The three files do not have the same number of lines!")

quran_data = []
for a_line, e_line, b_line in zip(arabic_lines, english_lines, bengali_lines):
    a_parts = a_line.split("|", 2)
    e_parts = e_line.split("|", 2)
    b_parts = b_line.split("|", 2)

    surah = int(a_parts[0])
    ayah = int(a_parts[1])
    arabic_text = a_parts[2].strip()
    english_text = e_parts[2].strip()
    bengali_text = b_parts[2].strip()

    quran_data.append({
        "surah": surah,
        "ayah": ayah,
        "arabic": arabic_text,
        "translation_en": english_text,
        "translation_bn": bengali_text
    })

# Save
with open("quran.json", "w", encoding="utf-8") as f:
    json.dump(quran_data, f, ensure_ascii=False, indent=2)

print(f"✅ Created quran.json with {len(quran_data)} ayahs")
