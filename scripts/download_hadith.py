import requests, json

URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari.json"

resp = requests.get(URL)
data = resp.json()

hadiths = []

for h in data["hadiths"]:
    hadiths.append({
        "collection": "Sahih Bukhari",
        "hadith_number": h["hadithnumber"],
        "chapter": h.get("chapter", ""),
        "text_en": h["text"],
        "grade": "Sahih"
    })

with open("data/hadith.json", "w", encoding="utf-8") as f:
    json.dump(hadiths, f, indent=2, ensure_ascii=False)

print(f"✅ Saved {len(hadiths)} hadiths")

