import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_documents_from_folder(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path)  # Sửa ở đây: đảm bảo truyền đúng string, không phải list
        else:
            print(f"❌ Bỏ qua file không hỗ trợ: {filename}")
            continue

        try:
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"⚠️ Lỗi khi load file {filename}: {e}")

    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)

def embed_and_save(documents, persist_directory):
    # Khởi tạo embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Tạo vectorstore với FAISS
    vectorstore = FAISS.from_documents(documents, embedding_model)

    # Lưu trữ vectorstore vào thư mục đích
    vectorstore.save_local(persist_directory)
    print(f"✅ Đã lưu vectorstore vào thư mục: {persist_directory}")

def load_and_process(folder_path, persist_directory):
    documents = load_documents_from_folder(folder_path)
    if not documents:
        print("❌ Không có tài liệu nào được load.")
        return

    chunks = split_documents(documents)
    embed_and_save(chunks, persist_directory)

