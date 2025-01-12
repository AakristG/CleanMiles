import os
import re
import json
from pdfminer.high_level import extract_text

# Input and output file paths
file_path = "backend/data/raw/Toyota2021.pdf"
output_folder = "backend/data/json"
output_file = os.path.join(output_folder, "Toyota2021_data.json")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' was not found!")

# Extract text from the PDF
text = extract_text(file_path)

# Split text into lines
lines = text.split("\n")

# Split lines into left and right columns
midpoint = len(lines) // 2  # Approximate split
left_column = lines[:midpoint]
right_column = lines[midpoint:]

# Combine columns for line-by-line processing
ordered_lines = left_column + right_column

# Regular expressions to match data
manufacturer_regex = r"^[A-Z\s]+$"  # Matches lines with manufacturer names (all uppercase)
model_regex = r"^[A-Za-z0-9\s\-]+$"  # Matches lines with model names (alphanumeric, spaces, hyphens)
mpg_city_hwy_regex = r"(\d{1,2}/\d{1,2})"  # Matches MPG (City/Hwy)
cost_regex = r"\$(\d{1,3}(?:,\d{3})+)"  # Matches annual fuel cost like "$2,900"
ghg_regex = r"\b(\d)\b"  # Matches GHG Rating (single digit)

# Initialize an empty list to store car data
car_data = []

# Parse the combined lines
manufacturer = None
model = None
unmatched_lines = []

for line in ordered_lines:
    line = line.strip()

    # Skip headers or irrelevant lines
    if "Manufacturer" in line or "Comb" in line or "Notes" in line or "Configuration" in line:
        continue

    # Check for manufacturer names
    if re.match(manufacturer_regex, line) and not line.isdigit():
        manufacturer = line
        continue

    # Check for model names
    if re.match(model_regex, line) and manufacturer:
        model = line
        continue

    # Extract MPG, cost, and GHG rating
    mpg_city_hwy_match = re.search(mpg_city_hwy_regex, line)
    cost_match = re.search(cost_regex, line)
    ghg_match = re.search(ghg_regex, line)

    if manufacturer and model:
        mpg_city_hwy = mpg_city_hwy_match.group(1) if mpg_city_hwy_match else "N/A"
        annual_fuel_cost = cost_match.group(0) if cost_match else "N/A"
        ghg_rating = ghg_match.group(1) if ghg_match else "N/A"

        car_data.append({
            "Manufacturer": manufacturer,
            "Model": model,
            "MPG (City/Hwy)": mpg_city_hwy,
            "Annual Fuel Cost": annual_fuel_cost,
            "GHG Rating": ghg_rating,
        })

        model = None
    else:
        unmatched_lines.append(line)

# Save the parsed data to a JSON file
os.makedirs(output_folder, exist_ok=True)
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(car_data, json_file, indent=4)

print(f"Data saved to {output_file}")

