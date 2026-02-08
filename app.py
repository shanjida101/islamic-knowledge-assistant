import streamlit as st
import streamlit.components.v1 as components
from router import route
from utils.pdf_export import export_results_to_pdf

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Islamic Knowledge Assistant",
    page_icon="🕌",
    layout="wide"
)

# =========================
# DISCLAIMER (safe HTML)
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
    height=330,
)

# =========================
# Sidebar
# =========================
st.sidebar.header("Settings")

language = st.sidebar.selectbox(
    "Qur’an Language",
    ["en", "bn"],
    key="quran_language_select"
)

top_k = st.sidebar.slider(
    "Results per source",
    min_value=1,
    max_value=5,
    value=3,
    key="top_k_slider"
)

st.sidebar.markdown("### Sources")

use_quran = st.sidebar.checkbox("Qur’an", value=True)
use_hadith = st.sidebar.checkbox("Hadith", value=False)
use_sharia = st.sidebar.checkbox("Sharia Principles", value=False)
use_hanafi = st.sidebar.checkbox("Hanafi Fiqh", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **About this project**
    - Multi-agent Islamic knowledge retrieval
    - Retrieval-only (no rulings generated)
    - Agents load on demand (Cloud-safe)
    """
)

# =========================
# User input
# =========================
question = st.text_input(
    "Ask a question",
    placeholder="e.g. prayer, hardship in Islam, intention in salah",
    key="question_input"
)

# =========================
# Results
# =========================
if question:
    if not any([use_quran, use_hadith, use_sharia, use_hanafi]):
        st.warning("Please select at least one source from the sidebar.")
    else:
        with st.spinner("Searching selected Islamic sources..."):
            results = route(
                question,
                lang=language,
                top_k=top_k,
                use_quran=use_quran,
                use_hadith=use_hadith,
                use_sharia=use_sharia,
                use_hanafi=use_hanafi,
            )

        st.markdown("---")

        for source, answers in results.items():
            st.markdown(f"## {source}")

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

        st.markdown("---")

        # =========================
        # PDF Export
        # =========================
        if st.button("📄 Export Results to PDF", key="export_pdf_button"):
            try:
                pdf_path = export_results_to_pdf(question, results)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=f,
                        file_name="islamic_ai_results.pdf",
                        mime="application/pdf",
                        key="download_pdf_button"
                    )
            except Exception:
                st.warning(
                    "PDF export is currently unavailable.\n\n"
                    "If you are running locally, make sure `reportlab` is installed."
                )
