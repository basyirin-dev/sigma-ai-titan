import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="SIGMA AI // TITAN",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --- CSS INJECTION ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# --- MISSION DASHBOARD ---
st.title("⚡ SIGMA AI // TITAN")
st.markdown("### SYSTEM STATUS: OPERATIONAL")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div class="titan-card">
        <h3>MODULE A: SOLVER</h3>
        <p>Multimodal First-Principles Engine.</p>
        <p><strong>STATUS: ONLINE</strong></p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="titan-card" style="opacity: 0.6;">
        <h3>MODULE B: ARCHIVE</h3>
        <p>Vectorized Knowledge Base.</p>
        <p><strong>STATUS: OFFLINE</strong></p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
    <div class="titan-card" style="opacity: 0.6;">
        <h3>MODULE C: ORACLE</h3>
        <p>RAG-Based Syllabus Expert.</p>
        <p><strong>STATUS: OFFLINE</strong></p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.divider()
st.info("Select a module from the sidebar to begin operation.")
