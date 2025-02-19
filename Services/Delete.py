

''' This module checks for data.jon file and if it is not there
it will return and say that the file is not there and if it is there 
it will delete the data given provide the id'''

import json
import os

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

def delete_user(user_id):
    data = load_data()
    if user_id in data:
        del data[user_id]
        save_data(data)
        return True
    return False
