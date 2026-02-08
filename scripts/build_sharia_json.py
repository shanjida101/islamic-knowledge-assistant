import json
import os

INPUT_FILE = "books/sharia/legal_maxims.txt"
OUTPUT_FILE = "data/sharia_principles.json"

os.makedirs("data", exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

data = []
buffer = []
counter = 1

for line in lines:
    line = line.strip()

    if len(line) == 0:
        continue

    buffer.append(line)

    # when buffer is long enough, treat as one entry
    if len(" ".join(buffer)) > 150:
        data.append({
            "id": counter,
            "text": " ".join(buffer),
            "source": "Legal Maxims of Islamic Jurisprudence"
        })
        counter += 1
        buffer = []

# catch leftover
if buffer:
    data.append({
        "id": counter,
        "text": " ".join(buffer),
        "source": "Legal Maxims of Islamic Jurisprudence"
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Created sharia_principles.json with {len(data)} entries")
