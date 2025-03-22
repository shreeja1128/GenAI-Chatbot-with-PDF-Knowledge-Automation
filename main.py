import streamlit as st
from app.chatbot import get_chat_response
from app.pdf_parser import extract_text_from_pdf

st.title("AskMyPDF")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
question = st.text_input("Ask a question about the document:")

if pdf_file and question:
    text = extract_text_from_pdf(pdf_file)
    response = get_chat_response(text, question)
    st.markdown(f"**Answer:** {response}")