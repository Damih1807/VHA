import streamlit as st
from query_utils import get_answer
import os
os.environ["STREAMLIT_WATCH_FILE_CHANGES"] = "false"

def main():
    st.title("Chat with your documents")

    question = st.text_input("Ask a question:")
    if question:
        answer = get_answer(question)
        st.success(answer)

if __name__ == "__main__":
    main()
