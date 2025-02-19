


''' This module checks for data.jon file and if it is not there
it will create /data.data.json file and write data into it and if 
it is there it wiil add the data given and write into it '''


import json
import os
import random

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    return data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def generate_id(data):
    # Generate a random two-digit id (10 to 99) and ensure uniqueness.
    while True:
        user_id = str(random.randint(10, 99))
        if user_id not in data:
            return user_id

def create_user(name, age, location):
    data = load_data()
    user_id = generate_id(data)
    data[user_id] = {
        'name': name,
        'age': age,
        'location': location
    }
    save_data(data)
    return user_id

