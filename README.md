📄 PDF-Based AI Question Answering System

Ask questions from your PDFs and get instant, accurate answers — all offline!

✨ Overview

Ever felt tired of going through PDFs again and again while revising notes?
I did. That’s why I built this PDF AI Q&A system.

It allows you to upload any PDF and ask questions about its content. The AI reads your document, finds the most relevant parts, and generates clear, contextual answers — without searching the internet or guessing.

It’s perfect for:

Students revising notes

Professionals working with technical/legal documents

Anyone who wants to extract knowledge from PDFs quickly

🧠 Features

✅ Upload a PDF and process it

✅ Split text into chunks and generate embeddings

✅ Store in FAISS vector database for fast retrieval

✅ Ask questions and get proper, context-aware answers

✅ Works fully offline after the initial model download

✅ Built with Python, LangChain, HuggingFace, FAISS, Streamlit

⚙️ How it Works

PDF Upload: User uploads a PDF

Processing: The system reads and splits content into chunks

Embeddings: Each chunk is converted into embeddings

Vector Store: FAISS stores chunks for fast similarity search

Question Answering: User asks a question → top chunks retrieved → AI generates answer

Flow Diagram:

PDF Upload → PDF Parser → Chunking → Embeddings → FAISS → User Question → Retrieve Chunks → LLM → Answer

🛠 Tech Stack

Python – main programming language

LangChain – for retrieval and chain management

FAISS – vector database for fast document search

HuggingFace Transformers – LLM & embeddings

Streamlit – simple web app interface

🚀 How to Run Locally

Clone the repo

git clone https://github.com/shreekarangupta/Smart-PDF-Question-Answering-AI
cd Smart-PDF-Question-Answering-AI


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py


Open your browser at http://localhost:8501 and upload a PDF to start asking questions.

🧪 Example Questions

If your PDF is about Machine Learning, you could ask:

What is supervised learning?

Explain overfitting in simple terms

Difference between classification and regression

If your PDF is legal notes:

What is IPC Section 420?

Explain fundamental rights

What is punishment under this act?

📌 Notes

Works offline after initial model download

AI answers are strictly based on uploaded documents only

You can improve the system by adding: multi-PDF support, voice input, or answer summaries

🤝 Contributions

Feel free to contribute or suggest improvements!

Bug fixes

Feature requests

UI improvements

📜 License


MIT License
