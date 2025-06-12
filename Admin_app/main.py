import os
from uploader import upload_file
from chunking import load_and_split
from embeddings import embed_and_save

UPLOAD_DIR = "data"
UPLOAD_FILENAME = "Hướng_dẫn_cách_viết_email_xin_nghỉ_phép_-VINOVA_2023__1_.pdf"
VECTOR_DIR = "vectorstore"

def main():
    file_path = upload_file(UPLOAD_DIR, UPLOAD_FILENAME)
    if file_path:
        chunks = load_and_split(file_path)
        embed_and_save(chunks, VECTOR_DIR)

if __name__ == "__main__":
    main()
