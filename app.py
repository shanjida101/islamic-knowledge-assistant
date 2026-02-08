import streamlit as st
import streamlit.components.v1 as components

from router import route

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Islamic Knowledge Assistant",
    page_icon="🕌",
    layout="wide"
)

# =========================
# Disclaimer (HTML, safe)
# =========================
components.html(
    """
    <div style="
        background-color:#ffe6e6;
        padding:20px;
        border-radius:12px;
        border-left:6px solid #cc0000;
        margin-bottom:24px;
        font-family: Inter, system-ui, sans-serif;
        max-width: 1100px;
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
    height=360,
)

# =========================
# Sidebar
# =========================
st.sidebar.header("Settings")

language = st.sidebar.selectbox(
    "Qur’an Language",
    ["en", "bn"],
    key="quran_language"
)

top_k = st.sidebar.slider(
    "Results per source",
    min_value=1,
    max_value=5,
    value=3,
    key="top_k"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **About this project**
    - Multi-agent Islamic knowledge retrieval
    - Sources: Qur’an, Hadith, Sharia principles, Hanafi fiqh
    - Retrieval-only (no rulings generated)
    - Agents load on demand (cloud-safe)
    """
)

# =========================
# User input
# =========================
question = st.text_input(
    "Ask a question",
    placeholder="e.g. prayer, hardship in Islam, intention in salah",
    key="question"
)

# =========================
# Results
# =========================
if question:
    with st.spinner("Searching classical Islamic sources..."):
        results = route(
            question,
            lang=language,
            top_k=top_k
        )

    st.markdown("---")

    for source, answers in results.items():
        if not answers:
            continue

        st.markdown(f"## {source}")

        for ans in answers:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #0f172a, #020617);
                    padding:18px;
                    margin-bottom:16px;
                    border-radius:10px;
                    border-left:5px solid #38bdf8;
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
    # PDF Export (optional)
    # =========================
    try:
        from utils.pdf_export import export_results_to_pdf

        if st.button("📄 Export Results to PDF", key="export_pdf"):
            pdf_path = export_results_to_pdf(question, results)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f,
                    file_name="islamic_knowledge_results.pdf",
                    mime="application/pdf",
                    key="download_pdf"
                )
    except Exception:
        st.info(
            "📄 PDF export is disabled.\n\n"
            "To enable locally:\n"
            "`pip install reportlab`"
        )
