import os
import csv
import numpy as np
import re

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

def sanitize_name(name):
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()  

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

def process_vehicle_data():
    """Process vehicle data from multiple CSV files and organize it into a structured directory format."""
    data_sources = [
        'backend/data/nodes/2021.csv',
        'backend/data/nodes/2022.csv',
        'backend/data/nodes/2023.csv',
        'backend/data/nodes/2024.csv',
        'backend/data/nodes/2025.csv',
    ]

    mpg_data_by_manufacturer = {}

    for source in data_sources:
        if not os.path.exists(source):
            print(f"Missing file: {source}")
            continue

        with open(source, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for entry in reader:
                brand = sanitize_name(entry['Mfr Name'].strip())
                model_name = sanitize_name(entry['Carline'].strip())
                production_year = entry['Model Year'].strip()
                city_efficiency = entry['City FE (Guide) - Conventional Fuel'].strip()
                highway_efficiency = entry['Hwy FE (Guide) - Conventional Fuel'].strip()
                combined_efficiency = entry['Comb FE (Guide) - Conventional Fuel'].strip()
                additional_152 = entry.get(reader.fieldnames[152], '').strip()
                additional_153 = entry.get(reader.fieldnames[153], '').strip()
                additional_154 = entry.get(reader.fieldnames[154], '').strip()

                # Skip rows with missing critical data
                if not (brand and model_name and production_year and city_efficiency and highway_efficiency and combined_efficiency):
                    print(f"Incomplete entry skipped: {entry}")
                    continue

                # Define directory structure
                brand_path = os.path.join('vehicles', brand)
                model_path = os.path.join(brand_path, model_name)

                os.makedirs(model_path, exist_ok=True)

                # Save data to a text file for the respective year
                year_data_file = os.path.join(model_path, f"{production_year}.txt")

                with open(year_data_file, 'w') as output_file:
                    output_file.write(f"{city_efficiency},{highway_efficiency},{combined_efficiency}\n")
                    output_file.write(f"{additional_152},{additional_153},{additional_154}\n")

                # Track values for computing averages
                if brand not in mpg_data_by_manufacturer:
                    mpg_data_by_manufacturer[brand] = {}

                if production_year not in mpg_data_by_manufacturer[brand]:
                    mpg_data_by_manufacturer[brand][production_year] = {
                        'city': [], 'highway': [], 'combined': [], 'additional_152': [], 'additional_153': [], 'additional_154': []
                    }

                mpg_data_by_manufacturer[brand][production_year]['city'].append(float(city_efficiency))
                mpg_data_by_manufacturer[brand][production_year]['highway'].append(float(highway_efficiency))
                mpg_data_by_manufacturer[brand][production_year]['combined'].append(float(combined_efficiency))
                if additional_152:
                    mpg_data_by_manufacturer[brand][production_year]['additional_152'].append(float(additional_152))
                if additional_153:
                    mpg_data_by_manufacturer[brand][production_year]['additional_153'].append(float(additional_153))
                if additional_154:
                    mpg_data_by_manufacturer[brand][production_year]['additional_154'].append(float(additional_154))

    # Generate extraInfo.txt files for organization
    generate_info_files('vehicles')

    # Save computed average values for each manufacturer and year
    for brand, yearly_data in mpg_data_by_manufacturer.items():
        save_average_data(os.path.join('vehicles', brand), yearly_data)


print("Folders and files created")
