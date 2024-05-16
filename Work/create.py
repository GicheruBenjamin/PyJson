
# Create a json file 
# Import json 
import json

# Create a Python dictionary
python_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert Python data to JSON and write to a file
with open('data.json', 'w') as json_file:
    json.dump(python_data, json_file)
    
# Create a json file that will be used for deletion operation
car = {
    "brand": "Toyota",
    "model": "Camry",
    "yop": 1994,
    "is_maintained": True
}

with open ('car.json', 'w') as json_file:
    json.dump(car, json_file)
