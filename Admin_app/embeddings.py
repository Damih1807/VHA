from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def embed_and_save(chunks, output_dir):
    # Tạo embeddings từ mô hình Hugging Face miễn phí
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Tạo FAISS vector store từ documents
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Lưu vector store vào thư mục
    vectorstore.save_local(output_dir)
