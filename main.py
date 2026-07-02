import streamlit as st

from src.llm import LLMmodel
from src.pipeline import legal_pipeline

def main():
    llm=LLMmodel()
    st.title("Hi! I am a Legal Assistant")
    st.caption("My knowledge base currently includes:\n1. The Consitution of India\n2. Securities and Exchange Board of India\n3. The Companies Act, 2013\n4. The Competition Act, 2002\n5. The Indian Contract Act, 1872\n6. The Insolvency and Bankruptcy Code (IBC), 2026")
    query=st.chat_input("Ask away!")
    if query:
        with st.chat_message("user"):
            st.write(query)

        response=legal_pipeline(query, llm)
        
        with st.chat_message("assistant"):
            st.write(response)


if __name__ == "__main__":
    main()
