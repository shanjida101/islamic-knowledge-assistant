import streamlit as st
from agents.quran_agent import QuranAgent
from agents.hadith_agent import HadithAgent
from agents.sharia_agent import ShariaAgent
from agents.hanafi_agent import HanafiAgent


@st.cache_resource(show_spinner=True)
def load_agent(name):
    if name == "quran":
        return QuranAgent()
    if name == "hadith":
        return HadithAgent()
    if name == "sharia":
        return ShariaAgent()
    if name == "hanafi":
        return HanafiAgent()


def route(question, lang="en", top_k=3):
    results = {}

    # Load agents ONLY when needed
    quran = load_agent("quran")
    hadith = load_agent("hadith")
    sharia = load_agent("sharia")
    hanafi = load_agent("hanafi")

    results["Qur'an"] = quran.answer(question, top_k, lang)
    results["Hadith"] = hadith.answer(question, top_k)
    results["Sharia Principles"] = sharia.answer(question, top_k)
    results["Hanafi Fiqh"] = hanafi.answer(question, top_k)

    return results
