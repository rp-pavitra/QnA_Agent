import duckdb
import pandas as pd

def get_connection():
    """
    Function to create a DuckDB database connection.

    Returns:
    conn (duckdb.DuckDBPyConnection): DuckDB database connection object.
    """
    conn = duckdb.connect('data.db')
    cursor = conn.cursor()
    return conn, cursor

def store_file_data_in_db(df, column_names):
    """
    Function to store DataFrame in DuckDB database.
    Parameters:
    df (DataFrame): The DataFrame to be stored in the database.
    """
    print("Storing file data in DuckDB database...")
    # Get DuckDB database connection
    conn, _ = get_connection()
    try:
        # Write DataFrame to DuckDB table
        conn.execute("DROP TABLE IF EXISTS file_data")
        columns_str = ', '.join([f'"{col}"' for col in column_names])
        conn.register('df_view', df)
        conn.execute(f"CREATE TABLE file_data AS SELECT {columns_str} FROM df_view")
        conn.unregister('df_view')
        conn.close()
        status = True
        print("File data stored in DuckDB database successfully.")
    except Exception as e:
        print(f"Error storing file data in DuckDB database: {str(e)}")
        status = False
        # conn.close()    
    return status

def get_schema():
    """
    Function to get the schema of the DuckDB database table.
    """
    conn, cursor = get_connection()
    print("Retrieving schema of the DuckDB table...")
    # Get the schema of the table
    cursor.execute("PRAGMA table_info('file_data')")
    schema = cursor.fetchall()
    conn.close()
    print("Schema retrieved successfully.")
    return schema
