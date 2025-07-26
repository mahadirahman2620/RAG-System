from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF

app = FastAPI()

class Query(BaseModel):
    question: str

# Load and preprocess the PDF
def extract_text(pdf_path):
    doc = fitz.open("C:\Users\MT\Downloads\rag_system")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

pdf_text = extract_text("HSC26-Bangla1st-Paper.pdf")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.create_documents([pdf_text])

# Create embedding and vector store
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/distiluse-base-multilingual-cased-v1")
db = FAISS.from_documents(chunks, embed_model)

# Mock function for answer generation (can be replaced with OpenAI or other LLM)
def generate_answer(context, question):
    return f"Based on the context: '{context[:300]}...', the answer to your question '{question}' is likely found there."

@app.post("/ask")
def ask_question(query: Query):
    docs = db.similarity_search(query.question, k=3)
    context = "\n\n".join([d.page_content for d in docs])
    response = generate_answer(context, query.question)
    return {"answer": response}
