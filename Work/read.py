
import json

# Open the JSON file and load its content
with open('data.json', 'r') as json_file:
    python_data = json.load(json_file)

print(python_data)

with open('car.json', 'r') as json_file:
    car = json.load(json_file)

print(car)