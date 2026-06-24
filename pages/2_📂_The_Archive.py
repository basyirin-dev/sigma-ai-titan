import streamlit as st

from utils import search_similar_problems

# The Archive - Vector Database for RAG
st.title("📂 The Archive")

# Search interface
search_query = st.text_input(
    "Search for similar problems:", placeholder="e.g., quadratic equations..."
)

if st.button("Search Archive"):
    if search_query:
        with st.spinner("Searching the archive..."):
            # Search vector database
            results = search_similar_problems(search_query)

            if results:
                st.markdown("### 📚 Similar Problems Found")
                for i, result in enumerate(results[:5]):  # Show top 5 results
                    with st.expander(
                        f"Problem {i + 1}: {result['metadata'].get('topic', 'Unknown')}"
                    ):
                        st.markdown(f"**Problem:** {result['content']}")
                        st.markdown(
                            f"**Solution:** {result['metadata'].get('solution', 'No solution available')}"
                        )
                        st.markdown(f"*Similarity Score: {result['score']:.2f}*")
            else:
                st.warning("No similar problems found in the archive.")
    else:
        st.warning("Please enter a search query.")
