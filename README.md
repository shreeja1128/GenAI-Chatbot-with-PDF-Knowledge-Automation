# AskMyPDF 📄💬

AskMyPDF is an intelligent, offline chatbot that allows users to **upload a PDF** and **ask questions** about its contents. Unlike typical GenAI tools that require paid APIs, this project uses **completely free and open-source models** from HuggingFace. It's perfect for students, researchers, or developers looking for private and cost-effective AI solutions.

---

## 🔍 Features

- 🧠 **Natural Language Q&A** powered by `distilbert-base-uncased-distilled-squad`
- 📄 **PDF Parsing** using `PyMuPDF` to extract text from any PDF
- 🔎 **Vector Search** with `FAISS` and `sentence-transformers` to find the most relevant content
- 💻 **User-Friendly Interface** built with `Streamlit`
- 🌐 **No Internet/API Required** once dependencies are installed
- ✅ Works offline and securely — your PDF never leaves your machine

---

## 🛠️ Technologies Used

| Area               | Tech Stack                                 |
|--------------------|---------------------------------------------|
| Language           | Python 3.8+                                 |
| Interface          | Streamlit                                   |
| NLP/Q&A Model      | `distilbert-base-uncased-distilled-squad`   |
| Embeddings         | `sentence-transformers` (MiniLM-L6-v2)      |
| Search Engine      | FAISS                                       |
| PDF Text Extraction| PyMuPDF (fitz)                              |
| Environment Mgmt   | `venv` (recommended)                        |

---

## 🧰 Folder Structure

```
AskMyPDF/
├── app/
│   ├── __init__.py              # Package initializer
│   ├── chatbot.py               # Question-answering logic (offline)
│   ├── pdf_parser.py            # Extracts text from PDF
│   ├── vector_store.py          # Vector DB creation with FAISS
│   └── config.py                # Placeholder (no key needed)
│
├── static/
│   └── style.css                # Optional styling
│
├── templates/
│   └── index.html               # Flask version (not used here)
│
├── main.py                     # Streamlit entry point
├── requirements.txt            # All required Python packages
├── README.md                   # This file
└── .gitignore                  # Ignored files
```

---

## 🚀 Setup Instructions

### 🔄 Step 1: Clone the repository
```bash
git clone https://github.com/shreeja1128/GenAI-Chatbot-with-PDF-Knowledge-Automation.git
cd GenAI-Chatbot-with-PDF-Knowledge-Automation
```

### 🐍 Step 2: Create & Activate a Virtual Environment (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 📦 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🧪 Step 4: Run the App
```bash
streamlit run main.py
```

Then open your browser to `http://localhost:8501`

---

## 🧪 Example Usage

1. Launch the app
2. Upload any PDF (e.g., a research paper or resume)
3. Ask questions like:
   - "What is the abstract?"
   - "Summarize the conclusion"
   - "What is the main topic?"

The app will use FAISS to find relevant chunks and answer using a distilled BERT QA model.

---

## 💡 How It Works (Under the Hood)

1. **PDF Upload**: User uploads a `.pdf`
2. **Text Extraction**: `PyMuPDF` extracts all text
3. **Chunking**: Text is split into manageable pieces
4. **Embedding**: Each chunk is converted into vector embeddings using `MiniLM`
5. **Vector Search**: FAISS retrieves chunks most relevant to the question
6. **Q&A Model**: `distilbert` answers the question based on the top relevant chunks

---

## 🌍 Offline & Secure
- ✅ No internet connection required after setup
- ✅ No API keys needed
- ✅ All processing is done locally on your machine

---

## 🧪 Example Models Used
- **Sentence Embedding Model**: `all-MiniLM-L6-v2`
- **Question-Answering Model**: `distilbert-base-uncased-distilled-squad`

Both are hosted on [Hugging Face](https://huggingface.co/), free and open-source.

---

## 🗂️ Git Workflow Used

```bash
cd AskMyPDF
# Initialize Git
git init

# Connect to GitHub repo
git remote add origin https://github.com/shreeja1128/GenAI-Chatbot-with-PDF-Knowledge-Automation.git

# Add and commit files
git add .
git commit -m "Initial commit: AskMyPDF offline GenAI chatbot"

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 📸 Screenshots (Optional)
<img width="1470" alt="Screenshot 2025-03-22 at 6 30 42 PM" src="https://github.com/user-attachments/assets/5c1e928b-c4d8-4101-8a19-895049fbfe27" />
<img width="1470" alt="Screenshot 2025-03-22 at 7 03 38 PM" src="https://github.com/user-attachments/assets/0357014f-f5a3-42ab-8b06-5c6f8c83a4f1" />
<img width="1470" alt="Screenshot 2025-03-22 at 6 25 49 PM" src="https://github.com/user-attachments/assets/6c904a73-1104-4448-9057-45d60c11bcd2" />
<img width="1470" alt="Screenshot 2025-03-22 at 6 27 21 PM" src="https://github.com/user-attachments/assets/84b32383-2109-43dd-8217-0c652e5409dc" />


---

## 📃 License
This project is open-source and free to use for educational or commercial purposes.

---

## 👤 Author
**Shreeja Konda**
