import streamlit as st
import streamlit.components.v1 as components
from agents.quran_agent import QuranAgent

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="Islamic Knowledge Assistant",
    page_icon="🕌",
    layout="wide"
)

# =========================
# Cache Quran agent ONLY
# =========================
@st.cache_resource(show_spinner=True)
def load_quran_agent():
    return QuranAgent()

quran_agent = load_quran_agent()

# =========================
# Title
# =========================
st.title("🕌 Islamic Knowledge Assistant")

# =========================
# DISCLAIMER (HTML iframe – reliable)
# =========================
components.html(
    """
    <div style="
        background-color:#ffe6e6;
        padding:20px;
        border-radius:10px;
        border-left:6px solid #cc0000;
        margin-bottom:20px;
        font-family: Inter, system-ui, sans-serif;
    ">
        <div style="color:#cc0000; font-size:20px; font-weight:700; margin-bottom:12px;">
            Important Disclaimer
        </div>

        <p style="color:#000000; font-size:15px; line-height:1.7;">
            This application is <strong>NOT</strong> a fatwa-issuing system.
            It is designed <strong>only for learning, study, and academic exploration</strong>
            of Islamic knowledge by retrieving information from classical sources such as
            the Qur’an, Hadith, Sharia principles, and Hanafi fiqh texts.
        </p>

        <p style="color:#000000; font-size:15px; line-height:1.7;">
            This system does <strong>not</strong> provide personal religious rulings,
            legal verdicts, or binding opinions.
            If you require a <strong>fatwa</strong> or religious guidance for real-life matters,
            please consult:
        </p>

        <ul style="margin-left:20px; color:#000000; font-size:15px;">
            <li>a qualified local imam or Islamic scholar</li>
            <li>a recognized fatwa institution (e.g. <strong>ifatwa.com</strong>)</li>
        </ul>

        <p style="color:#000000; font-size:15px; line-height:1.7;">
            Use this tool as a <strong>learning aid</strong>,
            not as a replacement for scholarly authority.
        </p>
    </div>
    """,
    height=320,
)

# =========================
# Sidebar
# =========================
st.sidebar.header("Settings")

language = st.sidebar.selectbox(
    "Qur’an Language",
    ["en", "bn"],
    key="lang"
)

top_k = st.sidebar.slider(
    "Results per source",
    min_value=1,
    max_value=5,
    value=3,
    key="topk"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **About this project**
    - Islamic knowledge retrieval
    - Source: Qur’an
    - Retrieval-only (no rulings generated)
    - Full multi-agent version runs locally
    """
)

# =========================
# User input
# =========================
question = st.text_input(
    "Ask a question",
    placeholder="e.g. prayer, guidance, patience",
)

# =========================
# Results
# =========================
if question:
    with st.spinner("Searching the Qur’an..."):
        answers = quran_agent.answer(question, top_k, language)

    st.markdown("## Qur’an")

    for ans in answers:
        st.markdown(
            f"""
            <div style="
                background-color:#111827;
                padding:16px;
                margin-bottom:14px;
                border-radius:8px;
                border-left:5px solid #3b82f6;
                color:#e5e7eb;
                line-height:1.7;
                font-size:15px;
            ">
                {ans}
            </div>
            """,
            unsafe_allow_html=True
        )
