import pandas as pd

from  db import store_file_data_in_db

def read_file(file):
    """Function to read an Excel file and return its content as a string."""

    df = pd.read_excel(file)
    file_content = df.to_string(index=False)
    print("successfull")

    return file_content,df


def load_file_main(file):
    """
    Function to load file data into the database.
    
    Parameters:
    file (str): The path to the file to be loaded.
    """
    _, df = read_file(file)
    return df

    # store_file_data_in_db(df)
    # print("File data loaded into the database successfully.")

# load_file_main("C:/Users/rppavitra/Downloads/UI Folder/ST/Forcast.xlsx")    