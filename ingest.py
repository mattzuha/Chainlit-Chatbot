from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Paths for data and vector storage
DATA_PATH = "data/"                         # Directory containing PDF and TXT documents
DB_FAISS_PATH = "vectorstores/db_faiss"     # Path to store the FAISS vector database

# Function to create and save a vector database
def create_vector_db():
    # Load PDF documents from the specified directory
    pdf_loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    pdf_documents = pdf_loader.load()  # Load all PDF files as documents

    # Load TXT documents from the specified directory
    txt_loader = DirectoryLoader(DATA_PATH, glob='*.txt', loader_cls=TextLoader)  # Load all TXT files as documents
    txt_documents = txt_loader.load()

    # Combine PDF and TXT documents into a single list
    documents = pdf_documents + txt_documents

    # Split documents into manageable text chunks for embedding
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Create embeddings for the text chunks and save them in a FAISS vector database
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(texts, embeddings)  # Generate embeddings and initialize FAISS
    db.save_local(DB_FAISS_PATH)  # Save FAISS database locally

# Run the create_vector_db function if this file is executed as a script
if __name__ == "__main__":
    create_vector_db()
