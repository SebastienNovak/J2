import pandas as pd

def process_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Process the DataFrame as needed
    # Example: df = df[df['column_name'] > 0]

    return df
