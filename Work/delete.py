import json

# Open the JSON file and load its content
with open('car.json', 'r') as json_file:
    car = json.load(json_file)

# Delete a key from the data
del car["model"]

# Write the updated data back to the file
with open('data.json', 'w') as json_file:
    json.dump(car, json_file)