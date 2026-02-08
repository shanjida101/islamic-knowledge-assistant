import json
import os
import re

INPUT_FILE = "books/hanafi/al_hidayah.txt"
OUTPUT_FILE = "data/hanafi_fiqh.json"

os.makedirs("data", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Remove page markers like "--- Page 12 ---"
text = re.sub(r"--- Page \d+ ---", "", text)

# Normalize spaces
text = re.sub(r"\s+", " ", text)

# Split into paragraphs using sentence boundaries
sentences = re.split(r"(?<=[.!?])\s+", text)

data = []
buffer = []
counter = 1

for s in sentences:
    buffer.append(s)

    # Create paragraph-sized chunks
    if len(" ".join(buffer)) > 300:
        data.append({
            "id": counter,
            "text": " ".join(buffer).strip(),
            "source": "Al-Hidayah (Hanafi fiqh)"
        })
        counter += 1
        buffer = []

# Catch leftover
if buffer:
    data.append({
        "id": counter,
        "text": " ".join(buffer).strip(),
        "source": "Al-Hidayah (Hanafi fiqh)"
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Created hanafi_fiqh.json with {len(data)} entries")
