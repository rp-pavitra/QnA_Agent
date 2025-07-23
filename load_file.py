import pandas as pd

from  db import store_file_data_in_db

def read_file(file):
    """Function to read an Excel file and return its content as a string."""

    # df = pd.read_excel(file)
    # file_content = df.to_string(index=False)
    
    df = pd.read_excel(file)
    df.to_csv("converted.csv", index=False)
    # Then, load the CSV fast
    df = pd.read_csv("converted.csv")
    file_content = df.to_string(index=False)
    print("successfull")

    return file_content,df


def load_file_main(file):
    """
    Function to load file data into the database.
    
    Parameters:
    file (str): The path to the file to be loaded.
    """
    # _, df = read_file(file)
    df = pd.read_excel(file, header=0, engine='openpyxl')
    print(df.head())
    column_names = df.columns.tolist()
    # Convert the 'Date' column to datetime, coercing errors to NaT
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    print("Columns in the DataFrame:", column_names)
    return df, column_names

    # store_file_data_in_db(df)
    # print("File data loaded into the database successfully.")

# load_file_main("C:/Users/rppavitra/Downloads/UI Folder/ST/Forcast.xlsx")    
