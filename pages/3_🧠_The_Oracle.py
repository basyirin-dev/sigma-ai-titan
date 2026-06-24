import streamlit as st

from utils import gemini_generate_content

# The Oracle - AI Tutor and Guide
st.title("🧠 The Oracle")

# Tutor mode selection
tutor_mode = st.selectbox(
    "Select Tutor Mode:",
    ["General Math Tutor", "Exam Prep", "Concept Explanation", "Practice Problems"],
)

# Input area
user_input = st.text_area(
    "Ask the Oracle:",
    height=100,
    placeholder="e.g., Explain calculus to me like I'm 10 years old...",
)

if st.button("🔮 Consult the Oracle"):
    if user_input:
        with st.spinner("The Oracle is consulting the stars..."):
            # Construct prompt based on mode
            prompt = f"""
            You are The Oracle, a wise and patient mathematics tutor.
            Mode: {tutor_mode}

            User question: {user_input}

            Provide:
            1. Clear, step-by-step explanation
            2. Relevant examples
            3. Helpful analogies or visualizations
            4. Common pitfalls to avoid
            5. Practice suggestions

            Be encouraging and make math feel approachable!
            """

            # Generate response using Gemini
            response = gemini_generate_content(prompt)

            # Display response
            st.markdown("### 💫 The Oracle Speaks")
            st.markdown(response)

            # Add to chat history
            if "oracle_history" not in st.session_state:
                st.session_state.oracle_history = []
            st.session_state.oracle_history.append(
                {"question": user_input, "response": response}
            )
    else:
        st.warning("Please ask the Oracle a question!")

# Chat history
if "oracle_history" in st.session_state and st.session_state.oracle_history:
    with st.expander("📜 Oracle History"):
        for i, item in enumerate(st.session_state.oracle_history[-5:]):
            st.markdown(f"**Q{i + 1}:** {item['question']}")
            st.markdown(f"*A{i + 1}:* {item['response'][:100]}...")
