

''' This module returns the updated data based 
on the id and the data given '''

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

def update_user(user_id, name=None, age=None, location=None):
    data = load_data()
    if user_id in data:
        if name:
            data[user_id]['name'] = name
        if age:
            data[user_id]['age'] = age
        if location:
            data[user_id]['location'] = location
        save_data(data)
        return True
    return False
