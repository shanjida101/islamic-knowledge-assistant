from agents.quran_agent import QuranAgent
from agents.hadith_agent import HadithAgent
from agents.sharia_agent import ShariaAgent
from agents.hanafi_agent import HanafiAgent

quran_agent = QuranAgent()
hadith_agent = HadithAgent()
sharia_agent = ShariaAgent()
hanafi_agent = HanafiAgent()


def route(question, lang="en", top_k=3):
    results = {
        "Qur'an": [],
        "Hadith": [],
        "Sharia Principles": [],
        "Hanafi Fiqh": []
    }

    # Qur'an
    for i, a in enumerate(quran_agent.answer(question, top_k, lang), start=1):
        results["Qur'an"].append(f"[Q-{i}] {a}")

    # Hadith
    for i, a in enumerate(hadith_agent.answer(question, top_k), start=1):
        results["Hadith"].append(f"[H-{i}] {a}")

    # Sharia
    for i, a in enumerate(sharia_agent.answer(question, top_k), start=1):
        results["Sharia Principles"].append(f"[S-{i}] {a}")

    # Hanafi
    for i, a in enumerate(hanafi_agent.answer(question, top_k), start=1):
        results["Hanafi Fiqh"].append(f"[F-{i}] {a}")

    return results
