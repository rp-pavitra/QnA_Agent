import sqlite3  
import pandas as pd  
  

def get_connection():
    """
    Function to create a SQLite database connection.
    
    Returns:
    conn (Connection): SQLite database connection object.
    """
    conn = sqlite3.connect('data.db')  
    cursor = conn.cursor()
    return conn,cursor


def store_file_data_in_db(df):
    """
    Function to store DataFrame in SQLite database.
    
    Parameters:
    df (DataFrame): The DataFrame to be stored in the database.
    """
    
    # Get SQLite database connection  
    conn,cursor = get_connection()

    # Convert the DataFrame to an SQL table  
    df.to_sql('file_data', conn, if_exists='replace', index=False)  
    
    # Close the connection  
    conn.close()  
    status = True
    return status


def get_schema():
    """
    Function to get the schema of the SQLite database table.
    """
    # Get SQLite database connection  
    conn,cursor = get_connection() 
    
    # Get the schema of the table  
    cursor.execute("PRAGMA table_info(file_data)")  
    schema = cursor.fetchall()  
    
    # Close the connection  
    conn.close()  
    
    return schema
  
