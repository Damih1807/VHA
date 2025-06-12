from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

VECTOR_DIR = "vectorstore"

def get_answer(query):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(VECTOR_DIR, embeddings)
    retriever = db.as_retriever()

    llm_pipeline = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=256)
    llm = HuggingFacePipeline(pipeline=llm_pipeline)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(query)
