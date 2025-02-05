import os
import csv
import numpy as np

# Directory where the structured data will be stored
base_dir = "backend/manufacturer"

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# List of CSV files
csv_files = [
    "backend/data/csv/Toyota2021.csv",
    "backend/data/csv/Toyota2022.csv",
    "backend/data/csv/Toyota2023.csv",
    "backend/data/csv/Toyota2024.csv",
    "backend/data/csv/Toyota2025.csv",
]

for csv_file in csv_files:
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        manufacturer = None 
        model = None 
        
        for row in reader:
            if not row:
                continue 

            line = row[0].strip() 
            
            if line.isupper(): 
                manufacturer = line
                manufacturer_dir = os.path.join(base_dir, manufacturer)
                os.makedirs(manufacturer_dir, exist_ok=True) 
            
            elif manufacturer and model is None: 
                model = line
                model_dir = os.path.join(manufacturer_dir, model)
                os.makedirs(model_dir, exist_ok=True) 
            
            elif manufacturer and model: 
                details_file = os.path.join(model_dir, "details.txt")
                with open(details_file, "w", encoding="utf-8") as details:
                    details.write(line + "\n")
                model = None 

def generate_info_files(root_dir):
    """Generate extraInfo.txt files for all levels after processing."""
    if os.path.exists(root_dir):
        # Write manufacturers extraInfo.txt
        manufacturers = [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]
        with open(os.path.join(root_dir, 'extraInfo.txt'), 'w') as info_file:
            info_file.write('\n'.join(manufacturers))

        # Write models and years extraInfo.txt
        for brand in manufacturers:
            brand_path = os.path.join(root_dir, brand)
            models = [name for name in os.listdir(brand_path) if os.path.isdir(os.path.join(brand_path, name))]
            with open(os.path.join(brand_path, 'extraInfo.txt'), 'w') as info_file:
                info_file.write('\n'.join(models))

            for model in models:
                model_path = os.path.join(brand_path, model)
                year_entries = [name.replace('.txt', '') for name in os.listdir(model_path) if name.endswith('.txt')]
                with open(os.path.join(model_path, 'extraInfo.txt'), 'w') as info_file:
                    info_file.write('\n'.join(year_entries))


def compute_mean(numbers):
    """Compute the mean of a list of numerical values."""
    return np.mean(numbers) if numbers else None


def save_average_data(brand_dir, yearly_data):
    """Save average values for each year in a dedicated averages directory."""
    avg_dir = os.path.join(brand_dir, 'averages')
    os.makedirs(avg_dir, exist_ok=True)

    yearly_files = []
    for year, mpg_data in yearly_data.items():
        avg_results = [compute_mean(mpg_data[key]) for key in mpg_data]
        avg_str_1 = ','.join([str(round(val, 2)) if val is not None else "N/A" for val in avg_results[:3]])
        avg_str_2 = ','.join([str(round(val, 2)) if val is not None else "N/A" for val in avg_results[3:]])
        avg_filename = f'{year}avg.txt'
        with open(os.path.join(avg_dir, avg_filename), 'w') as avg_file:
            avg_file.write(avg_str_1 + '\n')
            avg_file.write(avg_str_2 + '\n')
        yearly_files.append(avg_filename.replace('.txt', ''))

    # Write extraInfo.txt in averages folder
    with open(os.path.join(avg_dir, 'extraInfo.txt'), 'w') as info_file:
        info_file.write('\n'.join(yearly_files))


print("Folders and files created")
