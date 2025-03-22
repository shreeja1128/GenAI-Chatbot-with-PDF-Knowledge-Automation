from app.vector_store import get_vectorstore
from app.config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def get_chat_response(text, question):
    vectorstore = get_vectorstore(text)
    context = vectorstore.similarity_search(question, k=3)
    content = "\n".join([doc.page_content for doc in context])
    prompt = f"Answer the question based on the context:\nContext:\n{content}\n\nQuestion: {question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# --- app/pdf_parser.py ---
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
