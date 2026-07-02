import streamlit as st

from src.llm import LLMmodel
from src.pipeline import legal_pipeline

def main():
    llm=LLMmodel()
    st.title("Hi! I am a Legal Assistant")
    st.caption("The system currently supports question answering across the following Indian legal documents:\n1. The Constitution of India\n2. SEBI Regulations, 2015\n3. The Companies Act, 2013\n4. The Competition Act, 2002\n5. The Indian Contract Act, 1872\n6. The Insolvency and Bankruptcy Code (IBC), 2016")
    query=st.chat_input("Ask away!")
    if query:
        with st.chat_message("user"):
            st.write(query)

        response=legal_pipeline(query, llm)
        
        with st.chat_message("assistant"):
            st.write(response)


if __name__ == "__main__":
    main()
