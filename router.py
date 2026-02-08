import streamlit as st
from agents.quran_agent import QuranAgent
from agents.hadith_agent import HadithAgent
from agents.sharia_agent import ShariaAgent
from agents.hanafi_agent import HanafiAgent


# =========================
# Lazy-loaded agents
# =========================
@st.cache_resource(show_spinner=True)
def load_agent(agent_name):
    if agent_name == "quran":
        return QuranAgent()
    elif agent_name == "hadith":
        return HadithAgent()
    elif agent_name == "sharia":
        return ShariaAgent()
    elif agent_name == "hanafi":
        return HanafiAgent()
    else:
        raise ValueError(f"Unknown agent: {agent_name}")


# =========================
# Router
# =========================
def route(
    question,
    lang="en",
    top_k=3,
    use_quran=True,
    use_hadith=True,
    use_sharia=True,
    use_hanafi=True,
):
    results = {}

    if use_quran:
        quran = load_agent("quran")
        results["Qur’an"] = quran.answer(question, top_k, lang)

    if use_hadith:
        hadith = load_agent("hadith")
        results["Hadith"] = hadith.answer(question, top_k)

    if use_sharia:
        sharia = load_agent("sharia")
        results["Sharia Principles"] = sharia.answer(question, top_k)

    if use_hanafi:
        hanafi = load_agent("hanafi")
        results["Hanafi Fiqh"] = hanafi.answer(question, top_k)

    return results
