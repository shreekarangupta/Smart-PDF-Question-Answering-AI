import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import tempfile
import os

# ---------------- UI ----------------
st.set_page_config(page_title="PDF AI Q&A", layout="centered")
st.title("📄 PDF AI Question Answering System")
st.write("Upload a PDF and ask questions based only on its content.")

# ---------------- Upload PDF ----------------
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and processing PDF..."):

        # Save PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        # Load PDF
        loader = PyPDFLoader("notes.pdf")
        documents = loader.load()

        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)

        # Create embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Create FAISS vector store
        vectorstore = FAISS.from_documents(chunks, embeddings)

        # Load LLM
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

        pipe = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=512
        )

        llm = HuggingFacePipeline(pipeline=pipe)

        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False
        )

        st.success("PDF processed successfully! Ask your questions below.")

        # ---------------- Question Input ----------------
        question = st.text_input("Ask a question from the PDF:")

        if question:
            with st.spinner("Generating answer..."):
                answer = qa_chain.run(question)

            st.subheader("🧠 Answer:")
            st.write(answer)

        # Clean up
        os.remove(pdf_path)
