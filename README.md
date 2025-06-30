# QnA_Agent

1. app.py
    Purpose:
This is the main entry point of the Streamlit application.
It provides a user interface for uploading Excel files, processes the uploaded data, stores it in a database, and enables a Q&A chat interface powered by an AI agent.

    How to run the Agent:
 Type "streamlit run app.py" in the terminal
  
    Key Features:
-File upload (Excel .xlsx).
-Loads and stores file data in a database.
-Processes schema information.
-Maintains chat history using Streamlit’s session state.
-Handles user queries and displays AI-generated responses.


2. load_file.py
    Referenced Functions:
-load_file_main(uploaded_file): Loads and processes the uploaded Excel file.
-store_file_data_in_db(file_df): Stores the processed data into the database.
-read_file(file): Reads Excel file, returns string content and DataFrame

  Purpose:
-Handles file reading, data extraction, and database insertion logic.



3. db.py
    Referenced Function:
-get_schema(): Retrieves the database schema.
-get_connection():   Connects to SQLite DB and returns connection/cursor
-store_file_data_in_db(df):  Saves a DataFrame as a table in the DB, replacing if exists
-get_schema():   Retrieves the schema (columns) of the file_data table

    Purpose:
-Manages database connections and schema retrieval.


4. agent.py
    Referenced Function:
-get_agent_response(query, schema): Processes user queries using the AI agent and returns responses.

    Purpose:
    -Contains logic for interacting with the AI agent, using the schema to generate context-aware answers.
    -Imports Required libraries and functions
    -Azure OpenAI Setup  Credentials and client for Azure OpenAI
    -LLM Setup   Configures GPT-4 model for agent use
    -SQL Query Functions Executes SQL queries on SQLite database
    -Tool Definition Defines SQL execution tool for agent
    -Agent Initialization    Sets up LangChain agent with tools and LLM
    -get_agent_response  Handles user queries, invokes agent, returns response
