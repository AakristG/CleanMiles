import pandas as pd

def remove_blank_rows(input_file, output_file):
    df = pd.read_csv(input_file)

    # Drop blank rows
    df_cleaned = df.dropna(how='all')
    
    #Get rid of blank space in the front
    df = df.map(lambda x: x.lstrip() if isinstance(x, str) else x)

    df_cleaned.to_csv(output_file, index=False)

# Path to the CSV file
input_file = 'backend/data/csv/Toyota2025.csv' 
# Path to save the cleaned CSV file
output_file = 'backend/data/csv/cleaned_file.csv'
remove_blank_rows(input_file, output_file)
