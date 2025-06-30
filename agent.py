import streamlit as st
import os 
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from openai import AzureOpenAI
import pandas as pd
import sqlite3


from db import get_schema

# Set up Azure OpenAI credentials
AZURE_OPENAI_API_KEY2 = '<AZURE_OPENAI_API_KEY>'
AZURE_OPENAI_ENDPOINT2 = '<AZURE_OPENAI_ENDPOINT>'
OPENAI_DEPLOYMENT2= 'gpt-4-1106'
OPENAI_MODEL2= 'gpt-4'

client = AzureOpenAI(
  api_key = AZURE_OPENAI_API_KEY2,  
  api_version = "2023-05-15",
  azure_endpoint = AZURE_OPENAI_ENDPOINT2
)


llm_gpt4 = AzureChatOpenAI(
    model= OPENAI_MODEL2,
    openai_api_key = AZURE_OPENAI_API_KEY2,
    azure_endpoint = AZURE_OPENAI_ENDPOINT2,
    azure_deployment = OPENAI_DEPLOYMENT2,
    api_version = "2024-05-01-preview",  
    temperature=0)
llm = llm_gpt4

def sql_query(query: str):
    """Run a SQL SELECT query on a SQLite database and return the results."""
    with sqlite3.connect('data.db') as conn:
        return pd.read_sql_query(query, conn).to_dict(orient='records')
    

def sql_query_executor(query: str):
    """
    A tool that helps execute sql query based on Human natural language.
    """
    return sql_query(query)

# Tool definition
tools = [
    Tool(
        name="SQLQueryExecutor",
        func=sql_query_executor,
        description="This tool executes a SQL query based on Human natural language.",
    )
]    


# Creating the agent 
executor_step = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True,
    handle_parsing_errors=True,
    #memory=memory
)


def get_agent_response(human_query, schema):
    """
    Function to get the response from the agent based on the user query.
    """
    # Check if the user wants to exit
    if human_query.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        return "Exiting chat. Thank you!"
    
    system_prompt = f"""
    You are an expert SQL analyst. When appropriate, generate SQL queries based on the user question and the database schema.
    When you generate a query, use the 'sql_query' function to execute the query on the database and get the results.
    Then, use the results to answer the user's question.

    database_schema: [
        {schema}
    ]

    Once you get the response from the sql_query_executor tool, understand it and 
        give the desired response to the user.
        UserQuery : {human_query}

    sample human query: Give details of first 5 enteries of the table
    sql_query to be generated: SELECT * FROM file_data LIMIT 5
    response: df of first 5 enteries of table
    """.strip()

    # Invoke the agent with the system prompt
    log_response1 = executor_step.invoke(system_prompt)
    print(log_response1['output'])

    # Extract the final output from the agent's response
    final_output = log_response1['output']
    return final_output


# human_query = "give the sales details of the product HISSPL10HPCOPPER for the month of OCT"
# schema = get_schema()
# get_agent_response(human_query, schema)