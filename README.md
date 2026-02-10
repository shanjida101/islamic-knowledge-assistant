# 🕌 Islamic Multi-Agent Knowledge Assistant

A **source-grounded, multi-agent Islamic knowledge retrieval system** designed for
**learning, research, and academic exploration** of classical Islamic texts.

This project retrieves relevant passages from the **Qur’an, Hadith, Sharia legal maxims,
and Hanafi fiqh texts** using semantic search (FAISS + sentence embeddings).
It does **NOT** issue fatwas or personal religious rulings.

---

## ⚠️ Important Disclaimer

> **This system is NOT a fatwa-issuing tool.**  
> It does not provide religious verdicts, legal rulings, or binding opinions.  
>  
> The application is intended **only for education, study, and research** by retrieving
> information from classical Islamic sources.  
>  
> For authentic fatwas or personal religious guidance, consult:
> - a qualified local imam or Islamic scholar  
> - recognized fatwa institutions (e.g. **ifatwa.com**)  

Use this tool as a **learning aid**, not as a replacement for scholarly authority.

---

## 🎯 Project Objectives

- Build a **multi-agent system** where each agent represents a distinct Islamic source
- Ensure **zero hallucination** by using retrieval-only architecture
- Maintain **clear boundaries** between texts and religious authority
- Provide a **free, local, and transparent** system suitable for academic use

---

## 🧠 System Architecture

The system is composed of four independent agents:

| Agent | Source |
|-----|------|
| **Qur’an Agent** | Qur’anic verses (translations) |
| **Hadith Agent** | Authenticated Hadith collections |
| **Sharia Principles Agent** | Classical legal maxims (Qawāʿid Fiqhiyyah) |
| **Hanafi Agent** | Classical Hanafi fiqh texts (e.g. *Al-Hidayah*) |

Each agent:
- indexes its own corpus
- builds a FAISS vector index
- retrieves relevant passages independently

A central **router** queries all agents and aggregates results.

---

## 🏗️ Technical Stack

- **Python**
- **SentenceTransformers** (`all-MiniLM-L6-v2`)
- **FAISS (CPU)** for vector similarity search
- **Streamlit** for the user interface
- **Local JSON corpora** ( APIs)

---

## 📂 Project Structure

```text
agnets/
├── agents/
│   ├── base_agent.py
│   ├── quran_agent.py
│   ├── hadith_agent.py
│   ├── sharia_agent.py
│   └── hanafi_agent.py
│
├── books/
│   ├── sharia/
│   └── hanafi/
│
├── data/
│   ├── quran.json
│   ├── hadith.json
│   ├── sharia_principles.json
│   └── hanafi_fiqh.json
│
├── scripts/
│   ├── build_sharia_json.py
│   ├── build_hanafi_json.py
│   └── extract_hidayah_text.py
│
├── router.py
├── app.py
└── README.md
