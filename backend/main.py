import os
import re
import json
from pdfminer.high_level import extract_text

file_path = "backend/data/raw/Toyota2021.pdf"
output_folder = "backend/data/json"
output_file = os.path.join(output_folder, "Toyota2021_data.json")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' was not found!")

# Extract text from the PDF
text = extract_text(file_path)

# Regular expressions to match data
manufacturer_regex = r"^[A-Z\s]+$"  # Matches lines with manufacturer names (all uppercase)
model_regex = r"^[A-Za-z0-9\s\-]+$"  # Matches lines with model names (alphanumeric, spaces, hyphens)
mpg_regex = r"(\d{1,2}/\d{1,2})"  # Matches MPG (City/Hwy)
cost_regex = r"\$(\d{1,3}(?:,\d{3})*)"  # Matches annual fuel cost like "$2,920"
ghg_regex = r"\b(\d)\b"  # Matches GHG Rating (single digit)

# Initialize an empty list to store car data
car_data = []

lines = text.split("\n")
manufacturer = None
model = None

# Iterate over each line in the extracted text
for line in lines:
    line = line.strip()

    # Check for manufacturer names (lines with all uppercase letters)
    if re.match(manufacturer_regex, line):
        manufacturer = line.strip()
        continue

    # Check for model names (typically alphanumeric with spaces)
    if re.match(model_regex, line) and manufacturer:
        model = line.strip()
        continue

    # Extract MPG, fuel cost, and GHG rating
    mpg_match = re.search(mpg_regex, line)
    cost_match = re.search(cost_regex, line)
    ghg_match = re.search(ghg_regex, line)

    # If all required data is found, store it
    if mpg_match and cost_match and ghg_match and manufacturer and model:
        mpg = mpg_match.group(1)
        annual_fuel_cost = cost_match.group(0)
        ghg_rating = ghg_match.group(1)

        # Append data as a dictionary
        car_data.append({
            "Manufacturer": manufacturer,
            "Model": model,
            "MPG (City/Hwy)": mpg,
            "Annual Fuel Cost": annual_fuel_cost,
            "GHG Rating": ghg_rating
        })

        # Reset the model for the next car entry
        model = None

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Save the car data to a JSON file
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(car_data, json_file, indent=4)

print(f"Data successfully saved to {output_file}")
