import pandas as pd

def remove_blank_rows(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Drop rows that are entirely blank
    df_cleaned = df.dropna(how='all')
    
    df = df.map(lambda x: x.lstrip() if isinstance(x, str) else x)

    # Save the cleaned CSV file
    df_cleaned.to_csv(output_file, index=False)

# Usage
input_file = 'backend/data/csv/Toyota2021.csv'  # Path to the original messy CSV file
output_file = 'backend/data/csv/cleaned_file.csv'  # Path to save the cleaned CSV file
remove_blank_rows(input_file, output_file)
