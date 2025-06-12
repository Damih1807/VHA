import streamlit as st
from query_engine import get_answer

def main():
    st.title("💬 Chat with your documents")

    question = st.text_input("Ask a question:")
    if question:
        answer = get_answer(question)
        st.success(answer)

if __name__ == "__main__":
    main()
