# AskMyPDF

AskMyPDF is a smart chatbot powered by GenAI that allows users to upload PDF documents and ask questions about their contents. It uses OpenAI's GPT and LangChain to intelligently respond using the PDF context.

## 🚀 Features
- PDF text extraction using PyMuPDF
- Embedding + vector search via FAISS
- Question answering using OpenAI GPT
- Simple UI via Streamlit (Flask optional)

## 🛠️ Setup Instructions
```bash
pip install -r requirements.txt
```

Replace your OpenAI key in `app/config.py`, then run:
```bash
streamlit run main.py
```

## 📁 Folder Structure
```
AskMyPDF/
├── app/                  # Core logic (PDF parsing, chatbot, embeddings)
├── static/               # Optional styling
├── templates/            # Flask frontend (optional)
├── main.py               # Streamlit entry point
├── requirements.txt      # Dependencies
├── README.md             # Project overview
└── .gitignore            # Ignored files
```

## 📸 Screenshot (Optional)
Include a screenshot of your app here.

## 👤 Author
Shreeja Konda
