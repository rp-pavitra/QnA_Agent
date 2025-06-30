# QnA_Agent
Quick Overview
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

5. agent.py
    Referenced Function:
-get_agent_response(query, schema): Processes user queries using the AI agent and returns responses.
    Key Functional Areas:
   -Library Imports & Setup: Sets up required libraries and environment.
    -Azure OpenAI Configuration: Authenticates and connects to Azure OpenAI using credentials.
    -LLM Setup: Initializes GPT-4 model via LangChain.
    -SQL Execution Functions: Enables the agent to execute queries over the SQLite database.
    -Tool Definition: Defines tools (e.g., SQL executor) for the LangChain agent.
    -Agent Initialization :Assembles the agent with tools and model.
    -get_agent_response(query, schema): Accepts user query, uses LangChain to generate a response, and returns the result.



Setup Instructions

1. Clone the Repository
    cd QnA_Agent
2. Create Virtual Environment
    python -m venv venv
    On Windows: venv\Scripts\activate
3. Install Dependencies
    pip install -r requirements.txt
4. Set Environment Variables
    Create a .env file with your Azure OpenAI credentials:
    AZURE_OPENAI_API_KEY=your-api-key
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
    AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
    AZURE_OPENAI_API_VERSION=2023-05-15
    You may also directly modify the values in agent.py for quick testing.

5.Running the Application
    streamlit run app.py   


Usage Guidelines

1.Open the app in your browser.
2. Upload an Excel file (.xlsx).
3. Wait for schema extraction and confirmation.
4. Ask a natural language question about the uploaded data.
5. Receive a human-readable, AI-generated response.


    
