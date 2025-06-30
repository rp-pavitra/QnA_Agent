import streamlit as st

from load_file import load_file_main, store_file_data_in_db
from db import get_schema
from agent import get_agent_response 

def main():
    st.set_page_config("QnA Agent")
    st.title("AI Agent for QnA")
    st.write("Please upload your document to get started.")

    # File uploader for Excel files
    uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])

    # Checking if the file has been uploaded
    if uploaded_file:
        with st.spinner("Loading and processing your document..."):
            file_df = load_file_main(uploaded_file)
            status = store_file_data_in_db(file_df)
            schema = get_schema()
            st.write("File data loaded into the database successfully.")

        if status and schema:
            st.success("File data loaded into the database successfully.")
        else:
            st.error("Error loading file data into the database. Please try again.")

        # Initializing chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Displaying chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        query = st.chat_input("Enter your query: ")
        if query:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": query})
            
            # Display user query
            with st.chat_message("user"):
                st.markdown(query)
            # Displaying a spinner while waiting for the response
            with st.spinner("Processing your query..."):
                st.write("Please wait while I process your query...")
                # Execute backend functions
                response = get_agent_response(query, schema)

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)
            
            # Store assistant response
            st.session_state.messages.append({"role": "assistant", "content": response})

    else:
        st.info("Please upload a valid file to proceed.")

if __name__ == "__main__":
    main()        