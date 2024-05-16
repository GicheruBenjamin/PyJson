
import json

# Open the JSON file and load its content
with open('data.json', 'r') as json_file:
    python_data = json.load(json_file)

# Update the data
python_data["age"] = 31

# Write the updated data back to the file
with open('data.json', 'w') as json_file:
    json.dump(python_data, json_file)