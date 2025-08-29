

import streamlit as st
from config import OPENAI_API_KEY
from file_handler import save_pdf
from indexer import create_index

st.title("LlamaIndex for RAG Implementation")
st.write("Upload PDF files and ask questions about them.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    file_path = save_pdf(uploaded_file)
    query_engine = create_index()

    if "user_query" not in st.session_state:
        st.session_state.user_query = ""
    if "response" not in st.session_state:
        st.session_state.response = ""

    st.session_state.user_query = st.text_input(
        "Ask a question about the PDF:", value=st.session_state.user_query
    )

    col1, col2 = st.columns(2)

    if col1.button("Submit"):
        if st.session_state.user_query.strip() != "":
            st.session_state.response = query_engine.query(st.session_state.user_query)
        else:
            st.warning("Please enter a question before submitting.")

    if col2.button("Clear"):
        st.session_state.user_query = ""
        st.session_state.response = ""

    if st.session_state.response:
        st.subheader("Answer:")
        st.write(st.session_state.response)

st.write("---")
st.write("This app uses LlamaIndex RAG to retrieve answers from uploaded PDFs.")
